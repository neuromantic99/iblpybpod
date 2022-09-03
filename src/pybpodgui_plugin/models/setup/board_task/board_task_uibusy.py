import logging

from PyQt5.QtGui import QIcon

import pyforms_generic_editor.resources as conf
from pybpodgui_plugin.models.setup.board_task.board_task_window import BoardTaskWindow

logger = logging.getLogger(__name__)


class BoardTaskUIBusy(BoardTaskWindow):
    """
    TODO
    """

    def __init__(self, setup):
        super(BoardTaskUIBusy, self).__init__(setup)
        self.__running_icon = QIcon(conf.PLAY_SMALL_ICON)

    def update_ui(self):
        pass
