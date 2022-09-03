import pybpodgui_plugin.settings as conf
import loggingbootstrap

__version__ = "1.4.2"

# setup different loggers but output to single file
loggingbootstrap.create_double_logger("pybpodgui_plugin_session_history", conf.APP_LOG_HANDLER_CONSOLE_LEVEL,
									  conf.APP_LOG_FILENAME,
									  conf.APP_LOG_HANDLER_FILE_LEVEL)
