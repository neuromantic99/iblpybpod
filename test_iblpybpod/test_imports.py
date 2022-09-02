import unittest


class TestImports(unittest.TestCase):

    def test_imports(self):
        import pybpodapi
        assert pybpodapi

        import loggingbootstrap
        assert loggingbootstrap

        import sca
        assert sca

        import one
        assert one

        import cv2
        assert cv2
