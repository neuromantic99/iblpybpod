import logging

import pybpodgui_plugin.settings as conf

__version__ = "1.8.2"
__author__ = "Carlos Mao de Ferro"
__credits__ = ["Carlos Mao de Ferro", "Ricardo Ribeiro", "Sérgio Copeto", 'Luís Teixeira']
__license__ = "MIT"
__maintainer__ = ["Carlos Mao de Ferro", "Ricardo Ribeiro", "Sérgio Copeto", 'Luís Teixeira']
__email__ = ["cajomferro@gmail.com", "ricardojvr@gmail.com", "sergio.copeto@research.fchampalimaud.org", 'micboucinha@gmail.com']
__status__ = "Development"

logging.basicConfig(filename=conf.APP_LOG_FILENAME, level=conf.APP_LOG_HANDLER_CONSOLE_LEVEL)

if conf.USE_MULTIPROCESSING:
    # https://docs.python.org/3.5/library/multiprocessing.html#multiprocessing.freeze_support
    from multiprocessing import freeze_support  # @UnresolvedImport
    freeze_support()
