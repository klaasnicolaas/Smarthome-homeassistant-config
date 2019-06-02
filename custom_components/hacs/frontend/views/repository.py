"""Serve HacsRepositoryView."""
# pylint: disable=broad-except
import logging
from aiohttp import web
from custom_components.hacs.blueprints import HacsViewBase

_LOGGER = logging.getLogger('custom_components.hacs.frontend')

LOVELACE_EXAMLE_URL = """
<pre id="LovelaceExample" class="yaml">
  - url: /community_plugin/{name}/{name}.js
</pre>
"""

LOVELACE_EXAMLE_URL_TYPE = """
<pre id="LovelaceExample" class="yaml">
  - url: /community_plugin/{name}/{name}.js
    type: {type}
</pre>
"""

class HacsRepositoryView(HacsViewBase):
    """Serve HacsRepositoryView."""

    name = "community_repository"

    def __init__(self):
        """Initilize."""
        self.url = self.url_path["repository"] + r"/{repository_id}"

    async def get(self, request, repository_id):
        """Serve HacsRepositoryView."""
        try:
            message = request.rel_url.query.get("message")
            repository = self.repositories[str(repository_id)]

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


            if repository.pending_restart:
                pending_restart = """
                    <div class='container''>
                        <div class="row">
                            <div class="col s12">
                                <div class="card-panel orange darken-4">
                                    <div class="card-content white-text">
                                        <span>
                                            You need to restart (and potentially reconfigure) Home Assisant, for your last operation to be loaded.
                                        </span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                """
            else:
                pending_restart = ""

            if repository.additional_info:
                if repository.info is None:
                    info = "</br>" + await self.aiogithub.render_markdown(repository.additional_info)
                    info = info.replace("<h3>", "<h6>").replace(
                        "</h3>", "</h6>"
                    )
                    info = info.replace("<h2>", "<h5>").replace(
                        "</h2>", "</h5>"
                    )
                    info = info.replace("<h1>", "<h4>").replace(
                        "</h1>", "</h4>"
                    )
                    info = info.replace("<code>", "<pre>").replace(
                        "</code>", "</pre>"
                    )
                    info = info.replace(
                        "<table>", "<table class='white-text'>"
                    )
                    info = info.replace("<ul>", "")
                    info = info.replace("</ul>", "")
                    repository.info = info
                else:
                    info = repository.info
            else:
                info = ""


            if repository.authors:
                authors = "<p>Author(s): "
                for author in repository.authors:
                    if "@" in author:
                        author = author.split("@")[-1]
                    authors += "<a href='https://github.com/{author}' target='_blank' style='margin: 2'> @{author}</a>".format(author=author)
                authors += "</p>"
            else:
                authors = ""

            if repository.repository_type == "integration":
                note = """
                    </br>
                    <i>
                        When installed, this will be located in '{}',
                        you still need to add it to your 'configuration.yaml' file.
                    </i></br></br>
                    <i>
                        To learn more about how to configure this,
                        click the "REPO" button to get to the repoistory for this integration.
                    </i>
                """.format(repository.local_path)
            else:
                if repository.javascript_type is None:
                    llnote = LOVELACE_EXAMLE_URL.format(name=repository.name)
                else:
                    llnote = LOVELACE_EXAMLE_URL_TYPE.format(name=repository.name, type=repository.javascript_type)
                note = """
                    </br><i>
                        When installed, this will be located in '{}',
                        you still need to add it to your lovelace configuration ('ui-lovelace.yaml' or the raw UI config editor).
                    </i>
                    </br></br>
                    <i>
                        When you add this to your configuration use this:
                    </i></br>
                        {}
                    <a title="Copy content to clipboard" id ="lovelacecopy" onclick="CopyToLovelaceExampleToClipboard()"><i class="fa fa-copy"></i></a>
                    </br></br><i>
                        To learn more about how to configure this,
                        click the "REPO" button to get to the repoistory for this plugin.
                    </i>
                """.format(repository.local_path, llnote)

            if not repository.installed:
                main_action = "INSTALL"
            elif repository.pending_update:
                main_action = "UPGRADE"
            else:
                main_action = "REINSTALL"

            if repository.repository_type == "plugin":
                if not repository.installed:
                    open_plugin = ""
                else:
                    if "lovelace-" in repository.name:
                        name = repository.name.split("lovelace-")[-1]
                    else:
                        name = repository.name
                    open_plugin = "<a href='/community_plugin/{}/{}.js' target='_blank'>OPEN PLUGIN</a>".format(repository.name, name)
            else:
                open_plugin = ""

            # Generate content
            content = self.base_content

            if repository.version_installed is not None:
                 inst_ver = "<p><b>Installed version:</b> {}</p>".format(repository.version_installed)
            else:
                inst_ver = ""

            if repository.last_release_tag is not None:
                 last_ver = "<p><b>Available version:</b> {}</p>".format(repository.last_release_tag)
            else:
                last_ver = ""

            if repository.last_updated is not None:
                 last_up = "<p><b>Last updated:</b> {}</p>".format(repository.last_updated)
            else:
                last_up = ""

            if repository.pending_update:
                changelog = "<a href='https://github.com/{}/releases' target='_blank'>CHANGELOG</a>".format(repository.repository_name)
            else:
                changelog = ""

            if repository.installed:
                uninstall = "<a href='{}/repository_uninstall/{}' style='float: right; color: #a70000; font-weight: bold;' onclick='ShowProgressBar()'>UNINSTALL</a>".format(self.url_path['api'], repository.repository_id)
            else:
                uninstall = ""

            content += """
                {}
                {}
                <div class='container''>
                    <div class="row">
                        <div class="col s12">
                            <div class="card blue-grey darken-1">
                                <div class="card-content white-text">
                                    <span class="card-title">
                                        {}
                                        <a href="{}/repository_update_repository/{}"
                                                style="float: right; color: #ffab40;" onclick="ShowProgressBar()">
                                            <i name="reload" class="fa fa-sync"></i>
                                        </a>
                                    </span>
                                    <p>{}</p></br>
                                    {}
                                    {}
                                    {}
                                    <span>{}</span>
                                    </br>
                                    {}
                                    {}
                                </div>
                                <div class="card-action">
                                    <a href="{}/repository_install/{}"
                                        onclick="ShowProgressBar()">
                                        {}
                                    </a>
                                    {}
                                    <a href='https://github.com/{}' target='_blank'>repository</a>
                                    {}
                                    {}
                                </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            """.format(custom_message, pending_restart, repository.name, self.url_path["api"], repository.repository_id,
                repository.description, inst_ver, last_ver, last_up, info, authors, note, self.url_path["api"],
                repository.repository_id, main_action, changelog, repository.repository_name, open_plugin, uninstall)

        except Exception as exception:
            _LOGGER.error(exception)
            raise web.HTTPFound(self.url_path["error"])

        return web.Response(body=content, content_type="text/html", charset="utf-8")