import pybpodgui_plugin.settings as conf
import logging

__version__ = "1.4.2"

logging.basicConfig(filename=conf.APP_LOG_FILENAME, level=conf.APP_LOG_HANDLER_CONSOLE_LEVEL)
# setup different loggers but output to single file
# loggingbootstrap.create_double_logger("pybpodgui_plugin_session_history", conf.APP_LOG_HANDLER_CONSOLE_LEVEL,
# 									  conf.APP_LOG_FILENAME,
# 									  conf.APP_LOG_HANDLER_FILE_LEVEL)
