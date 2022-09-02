import pyforms_generic_editor.settings as conf
from pybpodgui_plugin.models.projects.projects_treenode import ProjectsTreeNode

Projects = type(
    'Projects',
    tuple(conf.GENERIC_EDITOR_PLUGINS_FINDER.find_class('models.project.Projects') + [ProjectsTreeNode]),
    {}
)
