import unittest
import nbexec
from nbexec.core import NBExecError
from nbexec.cli import parse_args, run
import sys
import os

HERE =  os.path.dirname(os.path.abspath(__file__))

NBPATHS = [
    "simple-with-kernelspec.ipynb",
    "simple-without-kernelspec.ipynb"
]

notbook_dir = os.path.join(HERE, "notebooks")

notebooks = [ os.path.join(HERE, "notebooks", path)
    for path in NBPATHS ]

class NBExecTest(unittest.TestCase):

    def test_version(self):
        nbexec.__version__

    def test_basic(self):
        run([ notebooks[0] ])

    def test_kernelspec_error(self):
        with self.assertRaises(NBExecError) as context:
            run([ notebooks[1] ])
        run([ notebooks[1], "--kernel-name", "python3" ])

    def test_dir(self):
        run([ notbook_dir, "--kernel-name", "python3" ])

if __name__ == '__main__':
    unittest.main()
