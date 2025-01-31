import os

from flask import Flask, redirect

from vulnpy.flask.blueprint import vulnerable_blueprint

app = Flask(__name__)
app.register_blueprint(vulnerable_blueprint)


app.config["SESSION_COOKIE_SECURE"] = False
app.config["SESSION_COOKIE_HTTPONLY"] = False


@app.route("/")
def index():
    return redirect("/vulnpy/")


if os.environ.get("VULNPY_USE_CONTRAST"):
    from dongtai_agent_python.middlewares.flask_middleware import AgentMiddleware

    app.wsgi_app = AgentMiddleware(app.wsgi_app, app)
