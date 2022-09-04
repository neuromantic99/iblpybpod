from PyQt5 import QtCore
from PyQt5.QtWidgets import QTreeView, QFileSystemModel

from pyforms_gui.controls.control_base import ControlBase


class ControlFilesTree(ControlBase):
    def init_form(self):
        self._form = QTreeView()
        super(ControlFilesTree, self).init_form()

    @property
    def value(self): return self._value

    @value.setter
    def value(self, value):
        ControlBase.value.fset(self, value)
        model = QFileSystemModel(parent=None)
        self._form.setModel(model)
        model.setRootPath(QtCore.QDir.currentPath())

        self._form.setRootIndex(model.setRootPath(value))

        self._form.setIconSize(QtCore.QSize(32, 32))
