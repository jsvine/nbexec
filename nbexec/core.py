import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import os
import sys
import json
import logging

logging.basicConfig(
    format = "[%(asctime)s] %(message)s",
    datefmt = "%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger("nbexec")
logger.setLevel(logging.INFO)

DEFAULTS = {
    "timeout": None,
    "kernel_name": None,
    "stdout": False
}

class NBExecError(Exception):
    pass

def exec_nb(path, **kwargs):
    """
    Take a notebook and run it, using the 
    command-line arguments (when supplied).
    """

    settings = dict(DEFAULTS)
    settings.update(kwargs)

    logger.info("Executing {} ...".format(path))
    with open(path) as f:
        nb = nbformat.read(f, nbformat.NO_CONVERT)

    if "kernelspec" not in nb.metadata and settings["kernel_name"] is None:
        raise NBExecError("Kernel is neither specified in notebook {} nor supplied via --kernel-name.".format(path))

    kernel_name = settings["kernel_name"] or nb.metadata.kernelspec.name

    ep = ExecutePreprocessor(
        timeout = settings["timeout"],
        kernel_name = kernel_name
    )

    ep.preprocess(nb,  {
        "metadata": {
            "path": os.path.dirname(path)
        }
    })

    if settings["stdout"]:
        json.dump(nb, sys.stdout, indent = 2)
    else:
        with open(path, "w") as f:
            nbformat.write(nb, f)

def is_notebook(path):
    """
    Test (naively) whether a given path represents a Jupyter notebook.
    """
    return os.path.isfile(path) and path.split(".")[-1] == "ipynb"

def exec_dir(path, nb_kwargs, max_depth, current_depth):
    """
    Execute all notebooks in a directory, keeping track of how deep
    into the initially-specified directory we are.
    """
    if max_depth is not None and current_depth > max_depth:
        return

    for item in sorted(os.listdir(path)):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            exec_dir(full_path, nb_kwargs, max_depth, current_depth + 1)
        elif is_notebook(full_path):
            exec_nb(full_path, **nb_kwargs)
        else:
            pass
