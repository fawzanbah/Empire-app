import os
from engine.file_manager import FileManager

class Plugin:
    def _init_(self):
        self.files = FileManager()

    def run(self, topic, project):
        project_path = os.path.join("projects", project)
        os.makedirs(project_path, exist_ok=True)

        plan = f"""# Business Plan: {topic}

## Idea
This is an AI-generated business idea for {topic}.

## Steps
1. Research
2. Develop MVP
3. Launch
4. Market
5. Scale
"""
        self.files.save_file({"project": project, "file": "business_plan.md", "content": plan})
        return {"status":"Business plan generated", "files":["business_plan.md"]}