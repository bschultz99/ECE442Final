
from __future__ import unicode_literals
from __future__ import absolute_import, unicode_literals

import octoprint.plugin

class PrintSensorPlugin(octoprint.plugin.StartupPlugin, octoprint.pluginTemplatePlugin);
    def on_after_startup(self):
        self._logger.info("Hello world!")

__plugin_name__ = "Printer Sensors"
__plugin_version__ = "1.0.0"