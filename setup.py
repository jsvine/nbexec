from setuptools import setup
import os

NAME = "nbexec"
HERE = os.path.abspath(os.path.dirname(__file__))

version_ns = {}
with open(os.path.join(HERE, NAME, '__version__.py')) as f:
    exec(f.read(), {}, version_ns)

setup(
    name = NAME,
    version = version_ns['__version__'],
    description = "A dead-simple tool for executing Jupyter notebooks from the command line.",
    url = "http://github.com/jsvine/nbexec",
    author = "Jeremy Singer-Vine",
    author_email = "jsvine@gmail.com",
    license = "MIT",
    keywords = "jupyter",
    packages = [
        NAME
    ],
    install_requires = [
        "jupyter_client",
        "nbformat",
        "nbconvert"
    ],
    entry_points = {
        "console_scripts": [
            "nbexec = nbexec.cli:main"
        ]
    },
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
)
