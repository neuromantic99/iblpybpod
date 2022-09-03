import pyforms_generic_editor.settings as conf

from pybpodgui_plugin.models.session.session_uibusy import SessionUIBusy

Session = type(
    'Session',
    tuple(conf.GENERIC_EDITOR_PLUGINS_FINDER.find_class('models.session.Session') + [SessionUIBusy]), {}
)
