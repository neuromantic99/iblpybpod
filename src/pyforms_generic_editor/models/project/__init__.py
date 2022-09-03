import pyforms_generic_editor.settings as conf
from pyforms_generic_editor.models.project.generic_project import GenericProject

Project = type(
    'Project',
    tuple(conf.GENERIC_EDITOR_PLUGINS_FINDER.find_class('models.project.Project') + [GenericProject]),
    {}
)
