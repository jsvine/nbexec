import unittest
from nbexec.core import NBExecError
from nbexec.cli import parse_args, run
import sys
import os

HERE =  os.path.dirname(os.path.abspath(__file__))

NBPATHS = [
    "simple-with-kernelspec.ipynb",
    "simple-without-kernelspec.ipynb"
]

notebooks = [ os.path.join(HERE, "notebooks", path)
    for path in NBPATHS ]

class NBExecTest(unittest.TestCase):

    def test_basic(self):
        run([ notebooks[0] ])

    def test_kernelspec_error(self):
        with self.assertRaises(NBExecError) as context:
            run([ notebooks[1] ])
        run([ notebooks[1], "--kernel-name", "python3" ])

if __name__ == '__main__':
    unittest.main()
