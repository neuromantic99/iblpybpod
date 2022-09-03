import pyforms_generic_editor.settings as conf

from pybpodgui_plugin.models.setup.board_task.board_task_uibusy import BoardTaskUIBusy

BoardTask = type(
    'BoardTask',
    tuple(conf.GENERIC_EDITOR_PLUGINS_FINDER.find_class('models.setup.board_task.BoardTask') + [BoardTaskUIBusy]),
    {}
)
