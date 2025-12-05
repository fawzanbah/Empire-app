import os
from engine.file_manager import FileManager

class Plugin:
    def _init_(self):
        self.files = FileManager()

    def run(self, topic, project):
        # Create folder structure
        project_path = os.path.join("projects", project)
        os.makedirs(project_path, exist_ok=True)

        # Create basic HTML/CSS/JS
        html = f"""<!DOCTYPE html>
<html>
<head>
<title>{topic}</title>
<style>body{{font-family:Arial;padding:20px;}}</style>
</head>
<body>
<h1>{topic}</h1>
<p>This is a generated website.</p>
</body>
</html>"""
        self.files.save_file({"project": project, "file": "index.html", "content": html})

        return {"status":"website generated", "files":["index.html"]}