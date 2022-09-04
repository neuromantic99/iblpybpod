import logging

from pybpodapi import settings as conf

__version__ = "1.8.2"
__author__ = [
    "Ricardo Ribeiro",
    "Carlos Mão de Ferro",
    "Joshua Sanders",
    "Luís Teixeira",
]
__credits__ = ["Ricardo Ribeiro", "Carlos Mao de Ferro", "Luís Teixeira"]
__license__ = "MIT"
__maintainer__ = [
    "Ricardo Ribeiro",
    "Carlos Mão de Ferro",
    "Joshua Sanders",
    "Luís Teixeira",
]
__email__ = [
    "ricardojvr@gmail.com",
    "cajomferro@gmail.com",
    "joshua21@gmail.com",
    "micboucinha@gmail.com",
]
__status__ = "Development"


# load the user settings
try:
    import user_settings
except:
    pass

if conf.PYBPOD_API_LOG_LEVEL is not None:
    logging.basicConfig(filename=conf.PYBPOD_API_LOG_FILE, level=conf.PYBPOD_API_LOG_LEVEL)
