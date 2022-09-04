import logging

import pybpodgui_plugin.settings as conf
from .stmdiagram_window import StmDiagramWindow

logging.basicConfig(filename=conf.APP_LOG_FILENAME, level=conf.APP_LOG_HANDLER_CONSOLE_LEVEL)


__version__ = "1.0.0"
__author__ = "Ricardo Jorge Vieira Ribeiro"
__credits__ = ["Ricardo Ribeiro"]
__license__ = "Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>"
__maintainer__ = ["Ricardo Ribeiro"]
__email__ = ["ricardo.ribeiro@research.fchampalimaud.org", "ricardojvr@gmail.com"]
__status__ = "Development"

