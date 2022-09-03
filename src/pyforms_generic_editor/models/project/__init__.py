from pyforms_generic_editor import settings as settingspy_conf
from pyforms_generic_editor.models.project.generic_project import GenericProject

Project = type(
    'Project',
    tuple(settingspy_conf.GENERIC_EDITOR_PLUGINS_FINDER.find_class('models.project.Project') + [GenericProject]),
    {}
)
