class SocialManager:
    def handle(self, data):
        action = data.get("action")
        project = data.get("project")
        # Example: save project as zip
        return {"status": f"Simulated {action} for {project}"}