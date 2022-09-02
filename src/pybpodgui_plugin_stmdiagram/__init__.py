import loggingbootstrap

from pybpodgui_plugin import settings as conf
from .stmdiagram_window import StmDiagramWindow

# setup different loggers but output to single file
loggingbootstrap.create_double_logger(
	"pybpodgui_plugin_stmdiagram",
	conf.APP_LOG_HANDLER_CONSOLE_LEVEL,
	conf.APP_LOG_FILENAME,
	conf.APP_LOG_HANDLER_FILE_LEVEL
)


__version__ = "1.0.0"
__author__ = "Ricardo Jorge Vieira Ribeiro"
__credits__ = ["Ricardo Ribeiro"]
__license__ = "Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>"
__maintainer__ = ["Ricardo Ribeiro"]
__email__ = ["ricardo.ribeiro@research.fchampalimaud.org", "ricardojvr@gmail.com"]
__status__ = "Development"

