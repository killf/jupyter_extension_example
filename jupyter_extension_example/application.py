import os

from .handlers import DefaultHandler
from jupyter_server.extension.application import ExtensionApp
from jupyter_server.extension.application import ExtensionAppJinjaMixin

DEFAULT_STATIC_FILES_PATH = os.path.join(os.path.dirname(__file__), "static")
DEFAULT_TEMPLATE_FILES_PATH = os.path.join(os.path.dirname(__file__), "templates")


class SimpleApp(ExtensionAppJinjaMixin, ExtensionApp):
    # The name of the extension.
    name = "jupyter_extension_example"

    # The url that your extension will serve its homepage.
    extension_url = "/jupyter_extension_example/default"

    # Should your extension expose other server extensions when launched directly?
    load_other_extensions = True

    # Local path to static files directory.
    static_paths = [DEFAULT_STATIC_FILES_PATH]

    # Local path to templates directory.
    template_paths = [DEFAULT_TEMPLATE_FILES_PATH]

    def initialize_handlers(self):
        self.handlers.extend(
            [
                (r"/{}/default".format(self.name), DefaultHandler)
            ]
        )

    def initialize_settings(self):
        pass


# -----------------------------------------------------------------------------
# Main entry point
# -----------------------------------------------------------------------------

main = launch_new_instance = SimpleApp.launch_instance
