import unittest
import os
from pathlib import Path


class TestImports(unittest.TestCase):
    import pybpodapi
    import confapp
    import loggingbootstrap
    import pyforms
    import sca


if __name__ == "__main__":
    iblpybpod_root_dir = Path(__file__).parent.parent

    # for x in os.walk(iblpybpod_root_dir):
    #     print("break")