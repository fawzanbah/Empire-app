import subprocess
import config

class DeployManager:
    def github(self, project):
        # simplified example: commit & push
        return {"status":"github deploy simulated"}

    def vercel(self, project):
        return {"status":"vercel deploy simulated"}

    def render(self, project):
        return {"status":"render deploy simulated"}

    def railway(self, project):
        return {"status":"railway deploy simulated"}

    def custom_url(self, project, url=None):
        return {"status":"custom deploy simulated","url":url or f"https://{project}.example.com"}