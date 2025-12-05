import os

class FileManager:
    def __init__(self, base_folder="projects"):
        self.base = base_folder
        if not os.path.exists(base_folder):
            os.makedirs(base_folder)

    def list_files(self, project):
        folder = os.path.join(self.base, project)
        if not os.path.exists(folder):
            return []
        return os.listdir(folder)

    def get_file(self, project, filename):
        path = os.path.join(self.base, project, filename)
        if not os.path.exists(path):
            return {"error":"File not found"}
        with open(path, "r", encoding="utf-8") as f:
            return {"content": f.read()}

    def save_file(self, data):
        project = data.get("project","default")
        filename = data.get("file")
        content = data.get("content","")
        folder = os.path.join(self.base, project)
        if not os.path.exists(folder):
            os.makedirs(folder)
        path = os.path.join(folder, filename)
        with open(path,"w",encoding="utf-8") as f:
            f.write(content)
        return {"status":"saved"}

    def new_file(self, data):
        project = data.get("project","default")
        filename = data.get("file")
        folder = os.path.join(self.base, project)
        if not os.path.exists(folder):
            os.makedirs(folder)
        path = os.path.join(folder, filename)
        with open(path,"w",encoding="utf-8") as f:
            f.write("")  # empty file
        return {"status":"created"}