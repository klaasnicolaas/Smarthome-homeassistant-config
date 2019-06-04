"""Serve HacsAPIView."""
# pylint: disable=broad-except
import logging
from aiohttp import web
from ...blueprints import HacsViewBase

_LOGGER = logging.getLogger('custom_components.hacs.frontend')


class HacsAPIView(HacsViewBase):
    """Serve HacsAPIView."""

    name = "community_api"

    def __init__(self):
        """Initilize."""
        self.url = self.url_path["api"] + r"/{element}/{action}"

    async def get(self, request, element, action=None):  # pylint: disable=unused-argument
        """Serve HacsAPIView."""
        _LOGGER.debug("GET API call for %s with %s", element, action)

        # Register new repository
        if element == "repository_install":
            repository = self.repositories[action]
            await repository.install()
            await self.storage.set()
            if action == "172733314":
                raise web.HTTPFound(self.url_path['settings'])
            raise web.HTTPFound("{}/{}".format(self.url_path['repository'], repository.repository_id))

        # Update a repository
        elif element == "repository_update_repository":
            repository = self.repositories[action]
            await repository.update()
            await self.storage.set()
            raise web.HTTPFound("{}/{}".format(self.url_path['repository'], repository.repository_id))

        # Update a repository
        elif element == "repository_update_settings":
            repository = self.repositories[action]
            await repository.update()
            await self.storage.set()
            raise web.HTTPFound(self.url_path['settings'])

        # Uninstall a element from the repository view
        elif element == "repository_uninstall":
            repository = self.repositories[action]
            await repository.uninstall()
            await self.storage.set()
            raise web.HTTPFound(self.url_path['store'])

        # Remove a custom repository from the settings view
        elif element == "repository_remove":
            repository = self.repositories[action]
            await repository.remove()
            await self.storage.set()
            raise web.HTTPFound(self.url_path['settings'])

        # Remove a custom repository from the settings view
        elif element == "repositories_reload":
            self.hass.async_create_task(self.update_repositories("Run it!"))
            raise web.HTTPFound(self.url_path['settings'])

        # Show content of hacs
        elif element == "hacs" and action == "inspect":
            jsons = {}
            skip = [
                "content_objects",
                "last_release_object",
                "repository",
            ]
            for repository in self.repositories:
                repository = self.repositories[repository]
                jsons[repository.repository_id] = {}
                var = vars(repository)
                for item in var:
                    if item in skip:
                        continue
                    jsons[repository.repository_id][item] = var[item]
            return self.json(jsons)

        elif element == "log" and action == "get":
            from ...handler.log import get_log_file_content
            content = self.base_content
            content += await get_log_file_content(self.config_dir)
            return web.Response(body=content, content_type="text/html", charset="utf-8")

        raise web.HTTPFound(self.url_path['error'])

    async def post(self, request, element, action=None):  # pylint: disable=unused-argument
        """Prosess POST API actions."""
        _LOGGER.debug("GET POST call for %s with %s", element, action)

        postdata = await request.post()

        if element == "repository_register":
            repository_name = postdata["custom_url"]
            repository_type = action

            # Stip first part if it's an URL.
            if "https://github" in repository_name:
                repository_name = repository_name.split("https://github.com/")[-1]

            if "https://www.github" in repository_name:
                repository_name = repository_name.split("https://www.github.com/")[-1]

            # If it still have content, continue.
            if repository_name != "":
                if repository_name in self.blacklist:
                    self.blacklist.remove(repository_name)
                repository, result = await self.register_new_repository(repository_type, repository_name)
                if result:
                    await self.storage.set()
                    raise web.HTTPFound("{}/{}".format(self.url_path['repository'], repository.repository_id))

            message = "Could not add {} at this time, check the log for more details.".format(repository_name)

            raise web.HTTPFound("{}?message={}".format(self.url_path['settings'], message))