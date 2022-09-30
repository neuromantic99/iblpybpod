import unittest


class TestImports(unittest.TestCase):

    def test_imports(self):
        import pybpodapi
        assert pybpodapi

        import sca
        assert sca

        import cv2
        assert cv2
