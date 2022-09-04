__version__ = "1.0.1"
__author__ = "Carlos Mão de Ferro"
__credits__ = ["Carlos Mão de Ferro", "Ricardo Ribeiro"]
__license__ = "Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>"
__maintainer__ = ["Carlos Mão de Ferro", "Ricardo Ribeiro"]
__email__ = ["cajomferro@gmail.com", "ricardojvr@gmail.com"]
__status__ = "Development"

import logging

from pybpodgui_plugin import settings as conf
from pybpodgui_plugin_timeline.trials_plot_window import TrialsPlotWindow as TrialsPlot

logging.basicConfig(filename=conf.APP_LOG_FILENAME, level=conf.APP_LOG_HANDLER_CONSOLE_LEVEL)
