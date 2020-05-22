from saleor.plugins.base_plugin import BasePlugin


class ExamplePlugin(BasePlugin):
    PLUGIN_ID = "mirumee.plugin.example"
    PLUGIN_NAME = "Example Plugin"
    PLUGIN_DESCRIPTION = "An example Saleor plugin."
    CONFIG_STRUCTURE = {}
    DEFAULT_CONFIGURATION = []
