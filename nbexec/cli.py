import argparse
import sys
import logging
from .core import (
    DEFAULTS,
    is_notebook,
    exec_nb,
    exec_dir,
    logger
)

def parse_args(args):
    parser = argparse.ArgumentParser(
        "nbexec",
        description = "Execute Jupyter notebooks on the command line.",
        epilog = "Note: nbexec uses Jupyter's nbconvert module. See https://nbconvert.readthedocs.io/en/latest/execute_api.html for context.",
        formatter_class = argparse.ArgumentDefaultsHelpFormatter,
        allow_abbrev = False
    )

    parser.add_argument(
        "notebooks",
        nargs = "+",
        help = "One or more notebooks, or directories containing notebooks."
    )

    parser.add_argument(
        "--max-depth",
        type = int,
        default = 1,
        help = "The number of directory levels to scan for notebooks."
    )

    parser.add_argument(
        "--timeout",
        type = int,
        default = DEFAULTS["timeout"],
        help = "How long to wait, in seconds, for any given notebook cell to before raising an exception."
    )

    parser.add_argument(
        "--kernel-name",
        default = DEFAULTS["kernel_name"],
        help = "The name of the kernel to use, e.g., 'python3'. If None, nbexec uses the kernel specified in the notebook."
    )

    parser.add_argument(
        "--quiet",
        action = "store_true",
        help = "Don't print notifications, other than errors."
    )

    parser.add_argument(
        "--stdout",
        action = "store_true",
        help = "Instead of saving the notebook in place, pipe the executed notebook to stdout. This option is not available if you are executing multiple notebooks at once."
    )

    parsed = parser.parse_args(args)

    if parsed.stdout:
        if len(parsed.notebooks) > 1 or not is_notebook(parsed.notebooks[0]):
            raise Exception("--stdout argument can only be used when executing a single notebook")
    
    return parsed

def run(args_raw):
    args = parse_args(args_raw)

    if args.quiet:
        logger.setLevel(logging.ERROR)

    for nb_path in args.notebooks:
        if is_notebook(nb_path):
            exec_nb(nb_path, **vars(args))
        elif os.path.isdir(nb_path):
            exec_dir(nb_path, vars(args), args.max_depth, 1)
        else:
            logger.info("Pathspec '{}' does not appear to be a Jupyter notebook or directory. Skipping.".format(nb_path))
    logger.info("Done.")

def main():
    run(sys.argv[1:])

if __name__ == "__main__":
    main()
