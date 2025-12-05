import os
import importlib

class AIRouter:
    def __init__(self, plugin_folder="plugins"):  # <-- Add this parameter
         self.plugin_folder = plugin_folder
         self.plugins = {}
         self.load_plugins()

    def load_plugins(self):
        if not os.path.exists(self.plugin_folder):
            os.makedirs(self.plugin_folder)

        for file in os.listdir(self.plugin_folder):
            if file.endswith(".py") and file != "_init_.py":
                name = file.replace(".py","")
                module_path = f"{self.plugin_folder.replace('/', '.')}.{name}"
                module = importlib.import_module(module_path)
                if hasattr(module, "Plugin"):
                    self.plugins[name] = module.Plugin()
                print(f"[AI ROUTER] Loaded plugin: {name}")

    def route(self, text):
        text = text.lower()
        if any(x in text for x in ["mobile app","android","ios","flutter"]):
            return "generator_mobile"
        if any(x in text for x in ["website","landing page","webpage","html"]):
            return "generator_web"
        if any(x in text for x in ["python","script","automation","api"]):
            return "generator_app"
        if any(x in text for x in ["business","startup","company","saas"]):
            return "generator_business"
        # fallback
        return "generator_api"

    def run_plugin(self, plugin_name, topic, project):
        if plugin_name not in self.plugins:
            return {"error":"Plugin not found"}
        return self.plugins[plugin_name].run(topic, project)