"""Blueprint for HacsBase."""
# pylint: disable=too-few-public-methods
import logging
import uuid
import os
from datetime import timedelta
from homeassistant.helpers.event import async_track_time_interval
from .aiogithub import AIOGitHubException
from .const import DEFAULT_REPOSITORIES

_LOGGER = logging.getLogger('custom_components.hacs.hacs')


class HacsBase:
    """The base class of HACS, nested thoughout the project."""
    const = None
    migration = None
    storage = None
    hacs = None
    data = {"hacs": {}}
    data["task_running"] = True
    hass = None
    config_dir = None
    aiogithub = None
    blacklist = []
    repositories = {}

    url_path = {}
    for endpoint in ["api", "error", "overview", "static", "store", "settings", "repository"]:
        url_path[endpoint] = "/community_{}-{}".format(str(uuid.uuid4()), str(uuid.uuid4()))

    async def startup_tasks(self):
        """Run startup_tasks."""
        from .hacsrepositoryintegration import HacsRepositoryIntegration
        self.data["task_running"] = True

        _LOGGER.info("Runing startup tasks.")

        # Store enpoints
        self.data["hacs"]["endpoints"] = self.url_path

        custom_log_level = {"custom_components.hacs": "debug"}
        await self.hass.services.async_call("logger", "set_level", custom_log_level)

        # For installed repositories only.
        async_track_time_interval(self.hass, self.recuring_tasks_installed, timedelta(minutes=30))

        # For the rest.
        async_track_time_interval(self.hass, self.update_repositories, timedelta(minutes=500))

        # Check for updates to HACS.
        repository = await self.aiogithub.get_repo("custom-components/hacs")
        repository = HacsRepositoryIntegration("custom-components/hacs", repository)
        await repository.setup_repository()
        self.repositories[repository.repository_id] = repository

        # After an upgrade from < 0.7.0 some files are missing.
        # This will handle that.
        checkpath = "{}/frontend/elements/all.min.css.gz".format(repository.local_path)
        if not os.path.exists(checkpath):
            _LOGGER.critical("HACS is missing files, trying to correct.")
            await repository.install()

        _LOGGER.info("Trying to load existing data.")

        # Check if migration is needed, or load existing data.
        await self.migration.validate()

        self.data["task_running"] = False

    async def register_new_repository(self, element_type, repo, repositoryobject=None):
        """Register a new repository."""
        from .exceptions import HacsBaseException, HacsRequirement
        from .blueprints import HacsRepositoryIntegration, HacsRepositoryPlugin

        _LOGGER.debug("Starting repository registration for %s", repo)

        if element_type == "integration":
            repository = HacsRepositoryIntegration(repo, repositoryobject)

        elif element_type == "plugin":
            repository = HacsRepositoryPlugin(repo, repositoryobject)

        else:
            return False

        setup_result = True
        try:
            await repository.set_repository()
            await repository.setup_repository()
        except (HacsRequirement, HacsBaseException, AIOGitHubException) as exception:
            _LOGGER.debug("%s - %s", repository.repository_name, exception)
            setup_result = False

        if setup_result:
            self.repositories[repository.repository_id] = repository

        else:
            if repo not in self.blacklist:
                self.blacklist.append(repo)
            _LOGGER.debug("%s - Could not register.", repo)
        return repository, setup_result

    async def update_repositories(self, now=None):
        """Run update on registerd repositories, and register new."""
        self.data["task_running"] = True

        _LOGGER.debug("Skipping repositories in blacklist %s", str(self.blacklist))

        # Running update on registerd repositories
        if self.repositories:
            for repository in self.repositories:
                try:
                    repository = self.repositories[repository]
                    if not repository.track or repository.repository_name in self.blacklist:
                        continue
                    if repository.hide and repository.repository_id != "172733314":
                        continue
                    if now is not None:
                        _LOGGER.info("Running update for %s", repository.repository_name)
                        await repository.update()
                except AIOGitHubException as exception:
                    _LOGGER.debug("%s - %s", repository.repository_name, exception)

        # Register new repositories
        integrations, plugins = await self.get_repositories()

        repository_types = {"integration": integrations, "plugin": plugins}

        for repository_type in repository_types:
            for repository in repository_types[repository_type]:
                if repository.archived:
                    continue
                elif repository.full_name in self.blacklist:
                    continue
                elif str(repository.id) in self.repositories:
                    repository = self.repositories[str(repository.id)]
                    await repository.update()
                else:
                    try:
                        await self.register_new_repository(repository_type, repository.full_name, repository)
                    except AIOGitHubException as exception:
                        _LOGGER.debug("%s - %s", repository.full_name, exception)
        await self.storage.set()
        self.data["task_running"] = False

    async def get_repositories(self):
        """Get defined repositories."""
        repositories = {}

        # Get org repositories
        repositories["integration"] = await self.aiogithub.get_org_repos("custom-components")
        repositories["plugin"] = await self.aiogithub.get_org_repos("custom-cards")

        # Additional repositories (Not implemented)
        for repository_type in DEFAULT_REPOSITORIES:
            for repository in DEFAULT_REPOSITORIES[repository_type]:
                result = await self.aiogithub.get_repo(repository)
                repositories[repository_type].append(result)

        return repositories["integration"], repositories["plugin"]

    async def recuring_tasks_installed(self, notarealarg):  # pylint: disable=unused-argument
        """Recuring tasks for installed repositories."""
        self.data["task_running"] = True
        _LOGGER.info("Running scheduled update of installed repositories")
        for repository in self.repositories:
            try:
                repository = self.repositories[repository]
                if not repository.track or repository.repository_name in self.blacklist:
                    continue
                if not repository.installed:
                    continue
                _LOGGER.info("Running update for %s", repository.repository_name)
                await repository.update()
            except AIOGitHubException as exception:
                _LOGGER.debug("%s - %s", repository.repository_name, exception)
        self.data["task_running"] = False

    @property
    def repositories_list_name(self):
        """Return a sorted(by name) list of repository objects."""
        repositories = []
        for repository in self.repositories:
            repositories.append(self.repositories[repository])
        return sorted(repositories, key=lambda x: x.name.lower())

    @property
    def repositories_list_repo(self):
        """Return a sorted(by repository_name) list of repository objects."""
        repositories = []
        for repository in self.repositories:
            repositories.append(self.repositories[repository])
        return sorted(repositories, key=lambda x: x.repository_name)
