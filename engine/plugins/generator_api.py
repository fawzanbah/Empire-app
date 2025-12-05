import os
from engine.file_manager import FileManager

class Plugin:
    def _init_(self):
        self.files = FileManager()

    def run(self, topic, project):
        project_path = os.path.join("projects", project)
        os.makedirs(project_path, exist_ok=True)

        api_py = f"""from flask import Flask, jsonify
app = Flask(_name_)

@app.route('/api')
def api_home():
    return jsonify({{"message":"{topic} API is live"}})

if _name_ == "_main_":
    app.run(port=5000)
"""
        self.files.save_file({"project": project, "file": "api.py", "content": api_py})
        return {"status":"API project generated", "files":["api.py"]}