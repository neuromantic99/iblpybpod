import logging

import pybpodgui_plugin.settings as conf

__version__ = "1.0.0"
__author__ = "Sérgio Copeto"
__credits__ = ["Sérgio Copeto", "Ricardo Ribeiro"]
__license__ = "Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>"
__maintainer__ = ["Sérgio Copeto", "Ricardo Ribeiro"]
__email__ = ["ricardojvr@gmail.com"]
__status__ = "Development"

logging.basicConfig(filename=conf.APP_LOG_FILENAME, level=conf.APP_LOG_HANDLER_CONSOLE_LEVEL)
