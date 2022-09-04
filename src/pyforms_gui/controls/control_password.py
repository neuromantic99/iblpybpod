from PyQt5.QtWidgets import QLineEdit

from pyforms_gui.controls.control_text import ControlText


class ControlPassword(ControlText):

    def init_form(self):
        super(ControlPassword, self).init_form()
        
        self.form.label.setAccessibleName('ControlPassword-label')
        self.form.lineEdit.setEchoMode(QLineEdit.Password)