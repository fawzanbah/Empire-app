import os
from engine.file_manager import FileManager

class Plugin:
    def _init_(self):
        self.files = FileManager()

    def run(self, topic, project):
        project_path = os.path.join("projects", project)
        os.makedirs(project_path, exist_ok=True)

        main_dart = f"""import 'package:flutter/material.dart';

void main() {{
  runApp(MaterialApp(
    home: Scaffold(
      appBar: AppBar(title: Text("{topic}")),
      body: Center(child: Text("Mobile app generated")),
    ),
  ));
}}
"""
        self.files.save_file({"project": project, "file": "main.dart", "content": main_dart})
        return {"status":"Flutter mobile app generated", "files":["main.dart"]}