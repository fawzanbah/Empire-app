from flask import Flask, request, jsonify, render_template_string
import os
from engine.ai_router import AIRouter
from engine.project_manager import ProjectManager
from engine.deploy_manager import DeployManager
from engine.social_manager import SocialManager
from engine.file_manager import FileManager

# ======================================
# INIT SYSTEM
# ======================================
app = Flask(__name__)

# Initialize modules
ai = AIRouter(plugin_folder="plugins")
projects = ProjectManager(base_folder="projects")
deploy = DeployManager()
files = FileManager("projects")
social = SocialManager()

# ======================================
# FRONTEND UI (Command + Preview)
# ======================================
frontend_html = """
<!DOCTYPE html>
<html>
<head>
  <title>ULTRA AI BUILDER</title>
  <style>
    body { font-family: Arial; margin: 20px; background: #f5f5f5; }
    #commandBox { width: 70%; padding: 10px; font-size: 16px; }
    #generateBtn { padding: 10px 20px; font-size: 16px; }
    iframe { width: 100%; height: 500px; border: 1px solid #ccc; margin-top: 20px; }
  </style>
</head>
<body>
  <h1>ULTRA AI BUILDER</h1>
  <input id="commandBox" placeholder="Type command e.g. build me an alarm app..." />
  <button id="generateBtn">Generate</button>

  <div>
    <h2>Project Preview</h2>
    <iframe id="previewFrame"></iframe>
  </div>

  <div>
    <h2>Deploy</h2>
    <button onclick="deploy('github')">Deploy to GitHub</button>
    <button onclick="deploy('vercel')">Deploy to Vercel</button>
    <button onclick="deploy('netlify')">Deploy to Netlify</button>
    <button onclick="deploy('render')">Deploy to Render</button>
    <button onclick="deploy('railway')">Deploy to Railway</button>
  </div>

  <script>
    const generateBtn = document.getElementById("generateBtn");
    generateBtn.onclick = async () => {
      const command = document.getElementById("commandBox").value;
      if(!command) return alert("Type a command first");

      const res = await fetch("/generate", {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({topic: command, project: "preview_project"})
      });
      const data = await res.json();
      alert("Generated using: " + data.plugin_used);

      // Load preview
      document.getElementById("previewFrame").src = "/projects/preview_project/index.html";
    };

    async function deploy(platform) {
      const res = await fetch("/deploy/" + platform, {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({project:"preview_project"})
      });
      const data = await res.json();
      alert("Deploy Status: " + JSON.stringify(data));
    }
  </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(frontend_html)


# ======================================
# FILE SYSTEM ROUTES
# ======================================
@app.get("/files/list")
def list_files():
    project = request.args.get("project", "default")
    return jsonify({"files": files.list_files(project)})

@app.get("/files/get")
def get_file():
    project = request.args.get("project")
    file = request.args.get("file")
    return files.get_file(project, file)

@app.post("/files/save")
def save_file():
    data = request.json
    return jsonify(files.save_file(data))

@app.post("/files/new")
def new_file():
    data = request.json
    return jsonify(files.new_file(data))


# ======================================
# GENERATE SYSTEM
# ======================================
@app.post("/generate")
def generate_anything():
    data = request.json
    topic = data.get("topic", "")
    project = data.get("project", "generated_app")

    plugin_name = ai.route(topic)
    output = ai.run_plugin(plugin_name, topic, project)

    return jsonify({
        "plugin_used": plugin_name,
        "project": project,
        "output": output
    })


# ======================================
# DEPLOY SYSTEM
# ======================================
@app.post("/deploy/github")
def deploy_github():
    project = request.json.get("project")
    return jsonify({"status": deploy.github(project)})

@app.post("/deploy/vercel")
def deploy_vercel():
    project = request.json.get("project")
    return jsonify({"status": deploy.vercel(project)})

@app.post("/deploy/netlify")
def deploy_netlify():
    project = request.json.get("project")
    return jsonify({"status": deploy.netlify(project)})

@app.post("/deploy/render")
def deploy_render():
    project = request.json.get("project")
    return jsonify({"status": deploy.render(project)})

@app.post("/deploy/railway")
def deploy_railway():
    project = request.json.get("project")
    return jsonify({"status": deploy.railway(project)})


# ======================================
# SOCIAL EXPORT
# ======================================
@app.post("/social/action")
def social_action():
    data = request.json
    return jsonify({"status": social.handle(data)})


# ======================================
# RUN SERVER
# ======================================
if __name__ == "_main_":
    if not os.path.exists("projects"):
        os.makedirs("projects")
    app.run(host="0.0.0.0", port=5000, debug=True)