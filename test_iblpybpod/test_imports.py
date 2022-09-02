import unittest


class TestImports(unittest.TestCase):

    def test_imports(self):
        import pybpodapi
        assert pybpodapi
        import confapp
        assert confapp
        import loggingbootstrap
        assert loggingbootstrap
        import pyforms
        assert pyforms
        import sca
        assert sca

