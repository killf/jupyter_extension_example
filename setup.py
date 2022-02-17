import os

from setuptools import setup
from jupyter_packaging import create_cmdclass

VERSION = "0.0.1"


def get_data_files():
    """Get the data files for the package."""
    data_files = [
        ("etc/jupyter/jupyter_server_config.d", "etc/jupyter/jupyter_server_config.d/", "*.json"),
    ]

    def add_data_files(path):
        for (dir_path, dir_names, file_names) in os.walk(path):
            if file_names:
                paths = [(dir_path, dir_path, filename) for filename in file_names]
                data_files.extend(paths)

    # Add all static and templates folders.
    add_data_files("jupyter_extension_example/static")
    add_data_files("jupyter_extension_example/templates")
    return data_files


cmd_class = create_cmdclass(data_files_spec=get_data_files())

setup_args = dict(
    name="jupyter_extension_example",
    version=VERSION,
    description="Jupyter Extension Example",
    long_description=open("README.md").read(),
    python_requires=">=3.7",
    install_requires=[
        "jupyter_server",
    ],
    include_package_data=True,
    cmdclass=cmd_class,
    entry_points={
        "console_scripts": [
            "jupyter-extension-example = jupyter_extension_example.application:main",
        ]
    },
)

if __name__ == "__main__":
    setup(**setup_args)
