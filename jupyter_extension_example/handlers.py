from jupyter_server.base.handlers import JupyterHandler
from jupyter_server.extension.handler import ExtensionHandlerMixin


class DefaultHandler(ExtensionHandlerMixin, JupyterHandler):
    def get(self):
        # The name of the extension to which this handler is linked.
        self.log.info("Extension Name in {} Default Handler: {}".format(self.name, self.name))
        # A method for getting the url to static files (prefixed with /static/<name>).
        self.log.info(
            "Static URL for / in simple_ext1 Default Handler: {}".format(self.static_url(path="/"))
        )
        self.write("<h1>Hello Simple 1 - I am the default...</h1>")
        self.write("Config in {} Default Handler: {}".format(self.name, self.config))
