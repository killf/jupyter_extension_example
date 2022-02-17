from .application import SimpleApp


def _jupyter_server_extension_paths():
    return [{"module": "jupyter_extension_example.application", "app": SimpleApp}]
