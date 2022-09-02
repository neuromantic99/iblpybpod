import pyforms_generic_editor.settings as conf
from pybpodgui_plugin.models.experiment.experiment_uibusy import ExperimentUIBusy

Experiment = type(
    'Experiment',
    tuple(conf.GENERIC_EDITOR_PLUGINS_FINDER.find_class('models.experiment.Experiment') + [ExperimentUIBusy]),
    {}
)
