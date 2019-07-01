"""Serve HacsAPIView."""
# pylint: disable=broad-except
import logging
from aiohttp import web
from ...blueprints import HacsViewBase
from ...exceptions import HacsRequirement
from ...aiogithub import AIOGitHubException

_LOGGER = logging.getLogger("custom_components.hacs.frontend")


class HacsAPIView(HacsViewBase):
    """Serve HacsAPIView."""

    name = "community_api"

    def __init__(self):
        """Initilize."""
        self.url = self.url_path["api"] + r"/{element}/{action}"

    async def get(
        self, request, element, action=None
    ):  # pylint: disable=unused-argument
        """Serve HacsAPIView."""
        _LOGGER.debug("GET API call for %s with %s", element, action)

        # Register new repository
        if element == "repository_install":
            repository = self.store.repositories[action]
            await repository.install()
            await self.storage.set()
            raise web.HTTPFound(
                "{}/{}".format(self.url_path["repository"], repository.repository_id)
            )

        # Update a repository
        elif element == "repository_update_repository":
            repository = self.store.repositories[action]
            await repository.update()
            await self.storage.set()
            raise web.HTTPFound(
                "{}/{}".format(self.url_path["repository"], repository.repository_id)
            )

        # Update a repository
        elif element == "repository_update_settings":
            repository = self.store.repositories[action]
            await repository.update()
            await self.storage.set()
            raise web.HTTPFound(self.url_path["settings"])

        # Uninstall a element from the repository view
        elif element == "repository_uninstall":
            repository = self.store.repositories[action]
            await repository.uninstall()
            await self.storage.set()
            raise web.HTTPFound(self.url_path["store"])

        # Remove a custom repository from the settings view
        elif element == "repository_remove":
            repository = self.store.repositories[action]
            await repository.remove()
            await self.storage.set()
            raise web.HTTPFound(self.url_path["settings"])

        # Hide a repository.
        elif element == "repository_hide":
            repository = self.store.repositories[action]
            repository.hide = True
            await self.storage.set()
            raise web.HTTPFound(self.url_path["store"])

        # Unhide a repository.
        elif element == "repository_unhide":
            repository = self.store.repositories[action]
            repository.hide = False
            await repository.update()
            await self.storage.set()
            raise web.HTTPFound(self.url_path["settings"])

        # Beta
        ## Show beta
        elif element == "repository_show_beta":
            repository = self.store.repositories[action]
            repository.show_beta = True
            await repository.update()
            await self.storage.set()
            raise web.HTTPFound(
                "{}/{}".format(self.url_path["repository"], repository.repository_id)
            )

        ## Hide beta
        elif element == "repository_hide_beta":
            repository = self.store.repositories[action]
            repository.show_beta = False
            await repository.update()
            await self.storage.set()
            raise web.HTTPFound(
                "{}/{}".format(self.url_path["repository"], repository.repository_id)
            )

        # Remove a custom repository from the settings view
        elif element == "repositories_reload":
            self.hass.async_create_task(self.update_repositories("Run it!"))
            raise web.HTTPFound(self.url_path["settings"])

        elif element == "repositories_upgrade_all":
            for repository in self.store.repositories:
                repository = self.store.repositories[repository]
                if repository.pending_update:
                    await repository.install()

            raise web.HTTPFound(self.url_path["settings"])

        # Show content of hacs
        elif element == "hacs" and action == "inspect":
            jsons = {}
            skip = ["content_objects", "last_release_object", "repository"]
            for repository in self.store.repositories:
                repository = self.store.repositories[repository]
                jsons[repository.repository_id] = {}
                var = vars(repository)
                for item in var:
                    if item in skip:
                        continue
                    jsons[repository.repository_id][item] = var[item]
            return self.json(jsons)

        raise web.HTTPFound(self.url_path["error"])

    async def post(
        self, request, element, action=None
    ):  # pylint: disable=unused-argument
        """Prosess POST API actions."""
        _LOGGER.debug("GET POST call for %s with %s", element, action)

        postdata = await request.post()

        if element == "frontend":
            if action == "view":
                self.store.frontend_mode = postdata["view_type"]
                self.store.write()
                raise web.HTTPFound(self.url_path["settings"])

        elif element == "repository_select_tag":
            repository = self.store.repositories[action]
            if postdata["selected_tag"] == repository.last_release_tag:
                repository.selected_tag = None
            else:
                repository.selected_tag = postdata["selected_tag"]
            try:
                await repository.update()
            except (AIOGitHubException, HacsRequirement):
                repository.selected_tag = repository.last_release_tag
                await repository.update()
                message = "The version {} is not valid for use with HACS.".format(postdata["selected_tag"])
                raise web.HTTPFound(
                    "{}/{}?message={}".format(self.url_path["repository"], repository.repository_id, message)
                )
            raise web.HTTPFound(
                "{}/{}".format(self.url_path["repository"], repository.repository_id)
            )

        elif element == "repository_register":
            repository_name = postdata["custom_url"]
            if "repository_type" in postdata:
                repository_type = postdata["repository_type"]
                _LOGGER.debug(
                    "GET POST call for %s with %s", repository_name, repository_type
                )

                # Stip first part if it's an URL.
                if "https://github" in repository_name:
                    repository_name = repository_name.split("https://github.com/")[-1]

                if "https://www.github" in repository_name:
                    repository_name = repository_name.split("https://www.github.com/")[
                        -1
                    ]

                # Strip whitespace
                repository_name = repository_name.split()[0]

                # If it still have content, continue.
                if repository_name != "":
                    if len(repository_name.split("/")) != 2:
                        message = "{} is not a valid format correct format is 'https://github.com/DEVELOPER/REPOSITORY' or 'DEVELOPER/REPOSITORY'.".format(
                            repository_name
                        )

                        raise web.HTTPFound(
                            "{}?message={}".format(self.url_path["settings"], message)
                        )
                    is_known_repository = await self.is_known_repository(
                        repository_name
                    )
                    if is_known_repository:
                        message = "{} is already registered, look for it in the store.".format(
                            repository_name
                        )
                        raise web.HTTPFound(
                            "{}?message={}".format(self.url_path["settings"], message)
                        )
                    if repository_name in self.blacklist:
                        self.blacklist.remove(repository_name)
                    repository, result = await self.register_new_repository(
                        repository_type, repository_name
                    )
                    if result:
                        await self.storage.set()
                        raise web.HTTPFound(
                            "{}/{}".format(
                                self.url_path["repository"], repository.repository_id
                            )
                        )

            message = "Could not add {} at this time, check the log for more details.".format(
                repository_name
            )

            raise web.HTTPFound(
                "{}?message={}".format(self.url_path["settings"], message)
            )
