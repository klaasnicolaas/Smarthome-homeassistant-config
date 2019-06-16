"""Serve HacsSettingsView."""
# pylint: disable=broad-except
import logging
from aiohttp import web
from homeassistant.const import __version__ as HAVERSION

from ...blueprints import HacsViewBase
from ...const import ISSUE_URL, NAME_LONG

_LOGGER = logging.getLogger('custom_components.hacs.frontend')


class HacsSettingsView(HacsViewBase):
    """Serve HacsSettingsView."""

    name = "community_settings"

    def __init__(self):
        """Initilize."""
        self.url = self.url_path["settings"]

    async def get(self, request):
        """Serve HacsOverviewView."""
        try:
            # We use these later:
            repository_lines = []
            hidden = []
            hacs = self.repositories.get("172733314")

            # Get the message sendt to us:
            message = request.rel_url.query.get("message")

            # HACS restart pending
            if hacs.pending_restart:
                hacs_restart = """
                    <div class='container'>
                        <div class="row">
                            <div class="col s12">
                                <div class="card-panel orange darken-4">
                                    <div class="card-content white-text">
                                        <span>
                                            You need to restart Home Assisant to start using the latest version of HACS.
                                        </span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                """
            else:
                hacs_restart = ""

            # HACS update pending
            if hacs.pending_update:
                hacs_update = """
                    <div class='container'>
                        <div class="row">
                            <div class="col s12">
                                <div class="card  red darken-4">
                                    <div class="card-content white-text">
                                        <span class="card-title">UPDATE PENDING</span>

                                        <p>There is an update pending for HACS!.</p>
                                        </br>
                                        <p><b>Current version:</b> {}</p>
                                        <p><b>Available version:</b> {}</p>
                                    </div>

                                    <div class="card-action">
                                        <a href="{}/repository_install/172733314" onclick="ShowProgressBar()">UPGRADE</a>
                                        <a href="https://github.com/custom-components/hacs/releases/tag/{}" target="_blank">CHANGELOG</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                """.format(hacs.version_installed, hacs.last_release_tag, self.url_path["api"], hacs.last_release_tag)
            else:
                hacs_update = ""

            if message != None:
                custom_message = """
                    <div class='container'>
                        <div class="row">
                            <div class="col s12">
                                <div class="card-panel orange darken-4">
                                    <div class="card-content white-text">
                                        <span>
                                            {}
                                        </span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                """.format(message)
            else:
                custom_message = ""


            # Repos:
            for repository in self.repositories_list_repo:
                if repository.hide and repository.repository_id != "172733314":
                    line = '<li class="collection-item hacscolor hacslist"><div>'
                    line += """
                        <a href="{}/repository_unhide/{}">
                        <i title="Unhide" class="fas fa-plus-circle" style="padding-right: 8px"></i></a> 
                        {}
                        <span class="repository-list-badge">{}</span>
                    """.format(self.url_path["api"], repository.repository_id, repository.repository_name, repository.repository_type)
                    line += "</div></li>"
                    hidden.append(line)

                if not repository.custom:
                    continue

                line = '<li class="collection-item hacscolor hacslist"><div>'
                line += """
                    <a href="{}/{}"><span class="repository-list-badge">{}</span> {}</a> 
                """.format(self.url_path["repository"], repository.repository_id, repository.repository_type, repository.repository_name)

                if repository.installed:
                    remove = """
                        <i title="Remove is not possible when {} is installed." class="secondary-content fas fa-trash-alt disabledaction"></i>
                    """.format(repository.repository_type)
                else:
                    remove = """
                        <a href={}/repository_remove/{} onclick="ShowProgressBar()" class="secondary-content" style="color: var(--primary-color)">
                            <i title="Remove." class="fas fa-trash-alt"></i>
                        </a>
                    """.format(self.url_path["api"], repository.repository_id)
                line += remove
                line += "</div></li>"


                repository_lines.append(line)

            # Generate content to display
            content = self.base_content
            content += """
                <div class='hacs-overview-container'>
                    {}
                    {}
                    {}
                </div>
            """.format(hacs_restart, hacs_update, custom_message)

            # HACS card
            content += """
                <div class='hacs-overview-container'>
                    <div class="hacs-card-standalone">
                        <h5>{}</h5>
                        <b>HACS version:</b> {}
                        {}</br>
                        <b>Home Assistant version:</b> {}</br>
                    </div>
                </div>
            """.format(NAME_LONG, hacs.version_installed, " <b>(RESTART PENDING!)</b>" if hacs.pending_restart else "", HAVERSION)

            # The buttons, must have buttons
            content += """
                <div class='hacs-overview-container'>
                    <a href="{}/repositories_reload/notinuse" class='waves-effect waves-light btn hacsbutton' onclick="ShowProgressBar()">
                        RELOAD DATA
                    </a>
                    <a href='{}/new/choose' class='waves-effect waves-light btn right hacsbutton' target="_blank">
                        OPEN ISSUE
                    </a>
                    <a href='https://github.com/custom-components/hacs' class='waves-effect waves-light btn right hacsbutton' target="_blank">
                        HACS REPO
                    </a>
                    <a href="{}/log/get" class='waves-effect waves-light btn right hacsbutton' onclick="ShowProgressBar()">
                        OPEN LOG
                    </a>
                </div>
            """.format(self.url_path["api"], ISSUE_URL, self.url_path["api"])

            ## Integration URL's
            content += """
                <div class='hacs-overview-container'>
                    <div class="row">
                        <ul class="collection with-header hacslist">
                            <li class="collection-header hacscolor hacslist"><h5>CUSTOM REPOSITORIES</h5></li>
            """
            for line in repository_lines:
                content += line
            content += """
                        </ul>
                        <form action="{}/repository_register/new" 
                                method="post" accept-charset="utf-8"
                                enctype="application/x-www-form-urlencoded">
                            <input id="custom_url" type="text" name="custom_url" 
                                    placeholder="ADD CUSTOM REPOSITORY" style="width: 70%; color: var(--primary-text-color)">

                            <select name="repository_type" class="repository-select">
                                <option disabled selected value>type</option>
                                <option value="integration">Integration</option>
                                <option value="plugin">Plugin</option>
                            </select>

                            <button class="btn waves-effect waves-light right" 
                                    type="submit" name="add" onclick="ShowProgressBar()" style="background-color: var(--primary-color); height: 44px;">
                                <i class="fas fa-save"></i>
                            </button>
                        </form>
                    </div>
                </div>
            """.format(self.url_path["api"])

            ## Hidden repositories
            if hidden:
                content += """
                    <div class='hacs-overview-container'>
                        <div class="row">
                            <ul class="collection with-header hacslist">
                                <li class="collection-header hacscolor hacslist"><h5>HIDDEN REPOSITORIES</h5></li>
                """
                for line in hidden:
                    content += line
                content += """
                            </ul>
                        </div>
                    </div>
                """

            content += self.footer

        except Exception as exception:
            _LOGGER.error(exception)
            raise web.HTTPFound(self.url_path["error"])

        return web.Response(body=content, content_type="text/html", charset="utf-8")
