import os
import sys
import traceback
from pathlib import Path

import logging

# IMPORTANT: used to import the user_settings.py file
sys.path.insert(0, os.getcwd())
import user_settings as user_settings_conf
logging.basicConfig(filename="app.log", level=logging.INFO)


try:
    # pyforms is imported here first time through pyforms
    # try:
    #     import user_settings
    # except ModuleNotFoundError:
    #     home = str(Path.home())
    #     home_settings_file = os.path.join(home, 'user_settings.py')
    #
    #     if not os.path.isfile(home_settings_file):
    #         with open(home_settings_file, 'w') as out:
    #             out.write("SETTINGS_PRIORITY = 0\n\n")
    #             out.write("GENERIC_EDITOR_PLUGINS_LIST = ['pybpodgui_plugin']")
    #
    #     sys.path.insert(0, home)
    #     import user_settings

    import pyforms_generic_editor.settings as conf

    # loggingbootstrap.create_double_logger(
    #     "pyforms_generic_editor",
    #     user_settings_conf.APP_LOG_HANDLER_CONSOLE_LEVEL,
    #     user_settings_conf.APP_LOG_FILENAME,
    #     user_settings_conf.APP_LOG_HANDLER_FILE_LEVEL
    # )
    #
    # loggingbootstrap.create_double_logger(
    #     "pyforms",
    #     user_settings_conf.APP_LOG_HANDLER_CONSOLE_LEVEL,
    #     user_settings_conf.APP_LOG_FILENAME,
    #     user_settings_conf.APP_LOG_HANDLER_FILE_LEVEL
    # )

    # pyforms.controls is imported here first time
    from pyforms_generic_editor.editor.base_editor import BaseEditor as Editor

except Exception as err:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    logging.getLogger().critical(str(err), exc_info=True)
    # logging.getLogger("pyforms_generic_editor").critical(str(err), exc_info=True)
    user_settings_conf.GENERIC_EDITOR_LOAD_EXCEPTION_TRACEBACK = traceback.format_exc()
    user_settings_conf.GENERIC_EDITOR_LOAD_EXCEPTION_LINE = exc_traceback.tb_lineno
    user_settings_conf.GENERIC_EDITOR_TITLE = 'PLEASE EDIT USER SETTINGS AND RESTART APP'

    from pyforms_generic_editor.editor.safe_mode_editor import SafeModeEditor as Editor


def start():
    from pyforms_gui import appmanager
    appmanager.start_app(Editor, conf.GENERIC_EDITOR_WINDOW_GEOMETRY)


if __name__ == '__main__':
    start()
