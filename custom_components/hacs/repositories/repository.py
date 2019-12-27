"""Repository."""
# pylint: disable=broad-except, bad-continuation, no-member
import pathlib
import json
import os
import tempfile
import zipfile
from integrationhelper import Validate, Logger
from aiogithubapi import AIOGitHubException
from .manifest import HacsManifest
from ..helpers.misc import get_repository_name
from ..hacsbase import Hacs
from ..hacsbase.backup import Backup
from ..handler.download import async_download_file, async_save_file
from ..helpers.misc import version_left_higher_then_right


RERPOSITORY_CLASSES = {}


def register_repository_class(cls):
    """Register class."""
    RERPOSITORY_CLASSES[cls.category] = cls
    return cls


class RepositoryVersions:
    """Versions."""

    available = None
    available_commit = None
    installed = None
    installed_commit = None


class RepositoryStatus:
    """Repository status."""

    hide = False
    installed = False
    last_updated = None
    new = True
    selected_tag = None
    show_beta = False
    track = True
    updated_info = False
    first_install = True


class RepositoryInformation:
    """RepositoryInformation."""

    additional_info = None
    authors = []
    category = None
    default_branch = None
    description = ""
    state = None
    full_name = None
    file_name = None
    javascript_type = None
    homeassistant_version = None
    last_updated = None
    uid = None
    stars = 0
    info = None
    name = None
    topics = []


class RepositoryReleases:
    """RepositoyReleases."""

    last_release = None
    last_release_object = None
    last_release_object_downloads = None
    published_tags = []
    objects = []
    releases = False


class RepositoryPath:
    """RepositoryPath."""

    local = None
    remote = None


class RepositoryContent:
    """RepositoryContent."""

    path = None
    files = []
    objects = []
    single = False


class HacsRepository(Hacs):
    """HacsRepository."""

    def __init__(self):
        """Set up HacsRepository."""

        self.content = RepositoryContent()
        self.content.path = RepositoryPath()
        self.information = RepositoryInformation()
        self.repository_object = None
        self.status = RepositoryStatus()
        self.state = None
        self.manifest = {}
        self.repository_manifest = HacsManifest.from_dict({})
        self.validate = Validate()
        self.releases = RepositoryReleases()
        self.versions = RepositoryVersions()
        self.pending_restart = False
        self.logger = None

    @property
    def pending_upgrade(self):
        """Return pending upgrade."""
        if self.status.installed:
            if self.status.selected_tag is not None:
                if self.status.selected_tag == self.information.default_branch:
                    if self.versions.installed_commit != self.versions.available_commit:
                        return True
                    return False
            if self.display_installed_version != self.display_available_version:
                return True
        return False

    @property
    def ref(self):
        """Return the ref."""
        if self.status.selected_tag is not None:
            if self.status.selected_tag == self.information.default_branch:
                return self.information.default_branch
            return "tags/{}".format(self.status.selected_tag)

        if self.releases.releases:
            return "tags/{}".format(self.versions.available)

        return self.information.default_branch

    @property
    def custom(self):
        """Return flag if the repository is custom."""
        if self.information.full_name.split("/")[0] in [
            "custom-components",
            "custom-cards",
        ]:
            return False
        if self.information.full_name in self.common.default:
            return False
        if self.information.full_name == "hacs/integration":
            return False
        return True

    @property
    def can_install(self):
        """Return bool if repository can be installed."""
        target = None
        if self.information.homeassistant_version is not None:
            target = self.information.homeassistant_version
        if self.repository_manifest is not None:
            if self.repository_manifest.homeassistant is not None:
                target = self.repository_manifest.homeassistant

        if target is not None:
            if self.releases.releases:
                if not version_left_higher_then_right(self.system.ha_version, target):
                    return False
        return True

    @property
    def display_name(self):
        """Return display name."""
        return get_repository_name(
            self.repository_manifest,
            self.information.name,
            self.information.category,
            self.manifest,
        )

    @property
    def display_status(self):
        """Return display_status."""
        if self.status.new:
            status = "new"
        elif self.pending_restart:
            status = "pending-restart"
        elif self.pending_upgrade:
            status = "pending-upgrade"
        elif self.status.installed:
            status = "installed"
        else:
            status = "default"
        return status

    @property
    def display_status_description(self):
        """Return display_status_description."""
        description = {
            "default": "Not installed.",
            "pending-restart": "Restart pending.",
            "pending-upgrade": "Upgrade pending.",
            "installed": "No action required.",
            "new": "This is a newly added repository.",
        }
        return description[self.display_status]

    @property
    def display_installed_version(self):
        """Return display_authors"""
        if self.versions.installed is not None:
            installed = self.versions.installed
        else:
            if self.versions.installed_commit is not None:
                installed = self.versions.installed_commit
            else:
                installed = ""
        return installed

    @property
    def display_available_version(self):
        """Return display_authors"""
        if self.versions.available is not None:
            available = self.versions.available
        else:
            if self.versions.available_commit is not None:
                available = self.versions.available_commit
            else:
                available = ""
        return available

    @property
    def display_version_or_commit(self):
        """Does the repositoriy use releases or commits?"""
        if self.releases.releases:
            version_or_commit = "version"
        else:
            version_or_commit = "commit"
        return version_or_commit

    @property
    def main_action(self):
        """Return the main action."""
        actions = {
            "new": "INSTALL",
            "default": "INSTALL",
            "installed": "REINSTALL",
            "pending-restart": "REINSTALL",
            "pending-upgrade": "UPGRADE",
        }
        return actions[self.display_status]

    async def common_validate(self):
        """Common validation steps of the repository."""
        # Attach helpers
        self.validate.errors = []
        self.logger = Logger(
            f"hacs.repository.{self.information.category}.{self.information.full_name}"
        )

        # Step 1: Make sure the repository exist.
        self.logger.debug("Checking repository.")
        try:
            self.repository_object = await self.github.get_repo(
                self.information.full_name
            )
        except Exception as exception:  # Gotta Catch 'Em All
            if not self.system.status.startup:
                self.logger.error(exception)
            self.validate.errors.append("Repository does not exist.")
            return

        # Step 2: Make sure the repository is not archived.
        if self.repository_object.archived:
            self.validate.errors.append("Repository is archived.")
            return

        # Step 3: Make sure the repository is not in the blacklist.
        if self.information.full_name in self.common.blacklist:
            self.validate.errors.append("Repository is in the blacklist.")
            return

        # Step 4: default branch
        self.information.default_branch = self.repository_object.default_branch

        # Step 5: Get releases.
        await self.get_releases()

        # Step 6: Get the content of hacs.json
        await self.get_repository_manifest_content()

        # Set repository name
        self.information.name = self.information.full_name.split("/")[1]

    async def common_registration(self):
        """Common registration steps of the repository."""
        # Attach logger
        if self.logger is None:
            self.logger = Logger(
                f"hacs.repository.{self.information.category}.{self.information.full_name}"
            )

        # Attach repository
        if self.repository_object is None:
            self.repository_object = await self.github.get_repo(
                self.information.full_name
            )

        # Set id
        self.information.uid = str(self.repository_object.id)

        # Set topics
        self.information.topics = self.repository_object.topics

        # Set stargazers_count
        self.information.stars = self.repository_object.attributes.get(
            "stargazers_count", 0
        )

        # Set description
        if self.repository_object.description:
            self.information.description = self.repository_object.description

    async def common_update(self):
        """Common information update steps of the repository."""
        # Attach logger
        if self.logger is None:
            self.logger = Logger(
                f"hacs.repository.{self.information.category}.{self.information.full_name}"
            )

        self.logger.debug("Getting repository information")

        # Attach repository
        self.repository_object = await self.github.get_repo(self.information.full_name)

        # Update description
        if self.repository_object.description:
            self.information.description = self.repository_object.description

        # Set stargazers_count
        self.information.stars = self.repository_object.attributes.get(
            "stargazers_count", 0
        )

        # Update default branch
        self.information.default_branch = self.repository_object.default_branch

        # Update last updaeted
        self.information.last_updated = self.repository_object.attributes.get(
            "pushed_at", 0
        )

        # Update topics
        self.information.topics = self.repository_object.topics

        # Update last available commit
        await self.repository_object.set_last_commit()
        self.versions.available_commit = self.repository_object.last_commit

        # Get the content of hacs.json
        await self.get_repository_manifest_content()

        # Update "info.md"
        await self.get_info_md_content()

        # Update releases
        await self.get_releases()

    async def install(self):
        """Common installation steps of the repository."""
        self.validate.errors = []
        persistent_directory = None

        await self.update_repository()

        if self.repository_manifest:
            if self.repository_manifest.persistent_directory:
                if os.path.exists(
                    f"{self.content.path.local}/{self.repository_manifest.persistent_directory}"
                ):
                    persistent_directory = Backup(
                        f"{self.content.path.local}/{self.repository_manifest.persistent_directory}",
                        tempfile.gettempdir() + "/hacs_persistent_directory/",
                    )
                    persistent_directory.create()

        if self.status.installed and not self.content.single:
            backup = Backup(self.content.path.local)
            backup.create()

        if self.repository_manifest.zip_release:
            validate = await self.download_zip(self.validate)
        else:
            validate = await self.download_content(
                self.validate,
                self.content.path.remote,
                self.content.path.local,
                self.ref,
            )

        if validate.errors:
            for error in validate.errors:
                self.logger.error(error)
            if self.status.installed and not self.content.single:
                backup.restore()

        if self.status.installed and not self.content.single:
            backup.cleanup()

        if persistent_directory is not None:
            persistent_directory.restore()
            persistent_directory.cleanup()

        if validate.success:
            if self.information.full_name not in self.common.installed:
                if self.information.full_name == "hacs/integration":
                    self.common.installed.append(self.information.full_name)
            self.status.installed = True
            self.versions.installed_commit = self.versions.available_commit

            if self.status.selected_tag is not None:
                self.versions.installed = self.status.selected_tag
            else:
                self.versions.installed = self.versions.available

            if self.information.category == "integration":
                if (
                    self.config_flow
                    and self.information.full_name != "hacs/integration"
                ):
                    await self.reload_custom_components()
                self.pending_restart = True

            elif self.information.category == "theme":
                try:
                    await self.hass.services.async_call("frontend", "reload_themes", {})
                except Exception:  # pylint: disable=broad-except
                    pass
            self.hass.bus.async_fire(
                "hacs/repository",
                {
                    "id": 1337,
                    "action": "install",
                    "repository": self.information.full_name,
                },
            )

    async def download_zip(self, validate):
        """Download ZIP archive from repository release."""
        try:
            contents = False

            for release in self.releases.objects:
                self.logger.info(f"ref: {self.ref}  ---  tag: {release.tag_name}")
                if release.tag_name == self.ref.split("/")[1]:
                    contents = release.assets

            if not contents:
                return validate

            for content in contents or []:
                filecontent = await async_download_file(self.hass, content.download_url)

                if filecontent is None:
                    validate.errors.append(f"[{content.name}] was not downloaded.")
                    continue

                result = await async_save_file(
                    f"{tempfile.gettempdir()}/{self.repository_manifest.filename}",
                    filecontent,
                )
                with zipfile.ZipFile(
                    f"{tempfile.gettempdir()}/{self.repository_manifest.filename}", "r"
                ) as zip_file:
                    zip_file.extractall(self.content.path.local)

                if result:
                    self.logger.info(f"download of {content.name} complete")
                    continue
                validate.errors.append(f"[{content.name}] was not downloaded.")
        except Exception:
            validate.errors.append(f"Download was not complete.")

        return validate

    async def download_content(self, validate, directory_path, local_directory, ref):
        """Download the content of a directory."""
        try:
            # Get content
            contents = []
            if self.releases.releases:
                for release in self.releases.objects:
                    if self.status.selected_tag == release.tag_name:
                        contents = release.assets
            if not contents:
                if self.content.single:
                    contents = self.content.objects
                else:
                    contents = await self.repository_object.get_contents(
                        directory_path, self.ref
                    )

            for content in contents:
                if content.type == "dir" and (
                    self.repository_manifest.content_in_root
                    or self.content.path.remote != ""
                ):
                    await self.download_content(
                        validate, content.path, local_directory, ref
                    )
                    continue
                if self.information.category == "plugin":
                    if not content.name.endswith(".js"):
                        if self.content.path.remote != "dist":
                            continue

                self.logger.debug(f"Downloading {content.name}")

                filecontent = await async_download_file(self.hass, content.download_url)

                if filecontent is None:
                    validate.errors.append(f"[{content.name}] was not downloaded.")
                    continue

                # Save the content of the file.
                if self.content.single:
                    local_directory = self.content.path.local

                else:
                    _content_path = content.path
                    if not self.repository_manifest.content_in_root:
                        _content_path = _content_path.replace(
                            f"{self.content.path.remote}/", ""
                        )

                    local_directory = f"{self.content.path.local}/{_content_path}"
                    local_directory = local_directory.split("/")
                    del local_directory[-1]
                    local_directory = "/".join(local_directory)

                # Check local directory
                pathlib.Path(local_directory).mkdir(parents=True, exist_ok=True)

                local_file_path = f"{local_directory}/{content.name}"
                result = await async_save_file(local_file_path, filecontent)
                if result:
                    self.logger.info(f"download of {content.name} complete")
                    continue
                validate.errors.append(f"[{content.name}] was not downloaded.")

        except Exception:
            validate.errors.append(f"Download was not complete.")
        return validate

    async def get_repository_manifest_content(self):
        """Get the content of the hacs.json file."""
        try:
            manifest = await self.repository_object.get_contents("hacs.json", self.ref)
            self.repository_manifest = HacsManifest.from_dict(
                json.loads(manifest.content)
            )
        except (AIOGitHubException, Exception):  # Gotta Catch 'Em All
            pass

    async def get_info_md_content(self):
        """Get the content of info.md"""
        from ..handler.template import render_template

        info = None
        info_files = ["info", "info.md"]

        if self.repository_manifest is not None:
            if self.repository_manifest.render_readme:
                info_files = ["readme", "readme.md"]
        try:
            root = await self.repository_object.get_contents("", self.ref)
            for file in root:
                if file.name.lower() in info_files:

                    info = await self.repository_object.get_contents(
                        file.name, self.ref
                    )
                    break
            if info is None:
                self.information.additional_info = ""
            else:
                info = info.content.replace("<svg", "<disabled").replace(
                    "</svg", "</disabled"
                )

                self.information.additional_info = render_template(info, self)

        except (AIOGitHubException, Exception):
            self.information.additional_info = ""

    async def get_releases(self):
        """Get repository releases."""
        if self.status.show_beta:
            self.releases.objects = await self.repository_object.get_releases(
                prerelease=True, returnlimit=self.configuration.release_limit
            )
        else:
            self.releases.objects = await self.repository_object.get_releases(
                prerelease=False, returnlimit=self.configuration.release_limit
            )

        if not self.releases.objects:
            return

        self.releases.releases = True

        self.releases.published_tags = []

        for release in self.releases.objects:
            self.releases.published_tags.append(release.tag_name)

        self.releases.last_release_object = self.releases.objects[0]
        if self.status.selected_tag is not None:
            if self.status.selected_tag != self.information.default_branch:
                for release in self.releases.objects:
                    if release.tag_name == self.status.selected_tag:
                        self.releases.last_release_object = release
                        break
        if self.releases.last_release_object.assets:
            self.releases.last_release_object_downloads = self.releases.last_release_object.assets[
                0
            ].attributes.get(
                "download_count"
            )
        self.versions.available = self.releases.objects[0].tag_name

    def remove(self):
        """Run remove tasks."""
        # Attach logger
        if self.logger is None:
            self.logger = Logger(
                f"hacs.repository.{self.information.category}.{self.information.full_name}"
            )
        self.logger.info("Starting removal")

        if self.information.uid in self.common.installed:
            self.common.installed.remove(self.information.uid)
        for repository in self.repositories:
            if repository.information.uid == self.information.uid:
                self.repositories.remove(repository)

    async def uninstall(self):
        """Run uninstall tasks."""
        # Attach logger
        if self.logger is None:
            self.logger = Logger(
                f"hacs.repository.{self.information.category}.{self.information.full_name}"
            )
        self.logger.info("Uninstalling")
        await self.remove_local_directory()
        self.status.installed = False
        if self.information.category == "integration":
            if self.config_flow:
                await self.reload_custom_components()
            else:
                self.pending_restart = True
        elif self.information.category == "theme":
            try:
                await self.hass.services.async_call("frontend", "reload_themes", {})
            except Exception:  # pylint: disable=broad-except
                pass
        if self.information.full_name in self.common.installed:
            self.common.installed.remove(self.information.full_name)
        self.versions.installed = None
        self.versions.installed_commit = None
        self.hass.bus.async_fire(
            "hacs/repository",
            {
                "id": 1337,
                "action": "uninstall",
                "repository": self.information.full_name,
            },
        )

    async def remove_local_directory(self):
        """Check the local directory."""
        import shutil
        from asyncio import sleep

        try:
            if self.information.category == "python_script":
                local_path = "{}/{}.py".format(
                    self.content.path.local, self.information.name
                )
            elif self.information.category == "theme":
                local_path = "{}/{}.yaml".format(
                    self.content.path.local, self.information.name
                )
            else:
                local_path = self.content.path.local

            if os.path.exists(local_path):
                self.logger.debug(f"Removing {local_path}")

                if self.information.category in ["python_script", "theme"]:
                    os.remove(local_path)
                else:
                    shutil.rmtree(local_path)

                while os.path.exists(local_path):
                    await sleep(1)

        except Exception as exception:
            self.logger.debug(f"Removing {local_path} failed with {exception}")
            return
