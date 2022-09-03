import pyforms_generic_editor.settings as conf

from pybpodgui_plugin.models.task.task_dockwindow import TaskDockWindow

Task = type(
    'Task',
    tuple(conf.GENERIC_EDITOR_PLUGINS_FINDER.find_class('models.task.Task') + [TaskDockWindow]),
    {}
)
