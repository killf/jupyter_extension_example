import os

from setuptools import setup

VERSION = "0.0.1"

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
)

if __name__ == "__main__":
    setup(**setup_args)
