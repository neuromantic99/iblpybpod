import loggingbootstrap

from pybpodgui_plugin import settings as settingpy_conf

__version__ = "1.8.2"
__author__ = "Carlos Mao de Ferro"
__credits__ = ["Carlos Mao de Ferro", "Ricardo Ribeiro", "Sérgio Copeto", 'Luís Teixeira']
__license__ = "MIT"
__maintainer__ = ["Carlos Mao de Ferro", "Ricardo Ribeiro", "Sérgio Copeto", 'Luís Teixeira']
__email__ = ["cajomferro@gmail.com", "ricardojvr@gmail.com", "sergio.copeto@research.fchampalimaud.org", 'micboucinha@gmail.com']
__status__ = "Development"

# setup different loggers but output to single file
loggingbootstrap.create_double_logger("pybpodgui_plugin", settingpy_conf.APP_LOG_HANDLER_CONSOLE_LEVEL,
                                      settingpy_conf.APP_LOG_FILENAME,
                                      settingpy_conf.APP_LOG_HANDLER_FILE_LEVEL)

loggingbootstrap.create_double_logger("pybranch", settingpy_conf.APP_LOG_HANDLER_CONSOLE_LEVEL,
                                      settingpy_conf.APP_LOG_FILENAME,
                                      settingpy_conf.APP_LOG_HANDLER_FILE_LEVEL)

loggingbootstrap.create_double_logger("pybpodapi", settingpy_conf.APP_LOG_HANDLER_CONSOLE_LEVEL,
                                      settingpy_conf.APP_LOG_FILENAME,
                                      settingpy_conf.APP_LOG_HANDLER_FILE_LEVEL)

if settingpy_conf.USE_MULTIPROCESSING:
    # https://docs.python.org/3.5/library/multiprocessing.html#multiprocessing.freeze_support
    from multiprocessing import freeze_support  # @UnresolvedImport
    freeze_support()
