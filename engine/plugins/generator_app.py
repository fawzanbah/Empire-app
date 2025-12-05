import os
from engine.file_manager import FileManager

class Plugin:
    def _init_(self):
        self.files = FileManager()

    def run(self, topic, project):
        project_path = os.path.join("projects", project)
        os.makedirs(project_path, exist_ok=True)

        app_py = f"""from flask import Flask, jsonify
app = Flask(_name_)

@app.route('/')
def home():
    return jsonify({{"message":"{topic} app running"}})

if _name_ == "_main_":
    app.run(port=5000)
"""
        self.files.save_file({"project": project, "file": "app.py", "content": app_py})
        return {"status":"Python/Flask app generated", "files":["app.py"]}