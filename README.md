[![Version](https://img.shields.io/pypi/v/nbexec.svg)](https://pypi.python.org/pypi/nbexec) [![Support Python versions](https://img.shields.io/pypi/pyversions/nbexec.svg)](https://pypi.python.org/pypi/nbexec)

# nbexec

`nbexec` is a dead-simple tool for executing Jupyter notebooks from the command line. It can run single notebooks, multiple notebooks, and/or an entire directory of notebooks in __one short command__.

`nbexec` runs your notebook using [Jupyter's (browserless) `nbconvert` execution API](http://nbconvert.readthedocs.io/en/latest/execute_api.html). Then, if the notebook ran without errors, `nbexec` resaves the notebook in place.

__Note:__ `nbexec` is in the early stages of development. Features may change/break in the future. Pinning your package installation to the current version is advised.

## Installation

```sh
pip install nbexec
```

## Basic usage

To run one notebook:

``` sh
nbexec path/to/my/notebook.ipynb
```

To run multiple notebooks:

``` sh
nbexec nb-one.ipynb foo/nb-two.ipynb
```

To run all notebooks in the first level of a directory:

``` sh
nbexec path/to/directory-of-notebooks
```

To run all notebooks in the first three levels of a directory:

``` sh
nbexec --max-depth 3 path/to/directory-of-notebooks
```

## Command-line options

``` 
usage: nbexec [-h] [--max-depth MAX_DEPTH] [--timeout TIMEOUT]
              [--kernel-name KERNEL_NAME] [--quiet] [--stdout]
              notebooks [notebooks ...]

Execute Jupyter notebooks on the command line.

positional arguments:
  notebooks             One or more notebooks, or directories containing
                        notebooks.

optional arguments:
  -h, --help            show this help message and exit
  --max-depth MAX_DEPTH
                        The number of directory levels to scan for notebooks.
                        (default: 1)
  --timeout TIMEOUT     How long to wait, in seconds, for any given notebook
                        cell to before raising an exception. (default: None)
  --kernel-name KERNEL_NAME
                        The name of the kernel to use, e.g., 'python3'. If
                        None, nbexec uses the kernel specified in the
                        notebook. (default: None)
  --quiet               Don't print notifications, other than errors.
                        (default: False)
  --stdout              Instead of saving the notebook in place, pipe the
                        executed notebook to stdout. This option is not
                        available if you are executing multiple notebooks at
                        once. (default: False)

Note: nbexec uses Jupyter's nbconvert module. See
https://nbconvert.readthedocs.io/en/latest/execute_api.html for context.
```

## Possible future features / improvements

- [ ] Full test coverage
- [ ] Option to ignore notebook execution errors (if executing multiple notebooks)
- [ ] [Your idea here]
