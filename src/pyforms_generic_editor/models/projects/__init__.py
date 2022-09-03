from pyforms_generic_editor import settings as settingspy_conf
from pyforms_generic_editor.models.projects.projects_dockwindow import ProjectsDockWindow as GenericProjects

Projects = type(
    'Projects',
    tuple(settingspy_conf.GENERIC_EDITOR_PLUGINS_FINDER.find_class('models.projects.Projects') + [GenericProjects]),
    {}
)
