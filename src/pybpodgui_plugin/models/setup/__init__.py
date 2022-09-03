import pyforms_generic_editor.settings as conf

from pybpodgui_plugin.models.setup.setup_uibusy import SetupUIBusy

Setup = type(
    'Setup',
    tuple(conf.GENERIC_EDITOR_PLUGINS_FINDER.find_class('models.setup.Setup') + [SetupUIBusy]),
    {}
)
