import os, shutil

class ProjectManager:
    def __init__(self, base_folder="projects"):
        self.base = base_folder
        if not os.path.exists(base_folder):
            os.makedirs(base_folder)

    def create_project(self, name):
        path = os.path.join(self.base, name)
        if os.path.exists(path):
            return {"error":"Project already exists"}
        os.makedirs(path)
        return {"status":"created","path":path}

    def delete_project(self, name):
        path = os.path.join(self.base, name)
        if os.path.exists(path):
            shutil.rmtree(path)
            return {"status":"deleted"}
        return {"error":"Project not found"}

    def get_project_path(self, name):
        return os.path.join(self.base, name)