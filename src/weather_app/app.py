from flask import Flask, render_template, request
from .weather import fetch_weather, parse_weather

def create_app() -> Flask:
    app = Flask(__name__, template_folder="../../templates")

    @app.route("/", methods=["GET", "POST"])
    def home():
        weather = None
        error = None

        if request.method == "POST":
            city = request.form.get("city", "").strip()
            data = fetch_weather(city)
            try:
                if data:
                    weather = parse_weather(data)
                else:
                    error = "Ville introuvable ou erreur API."
            except ValueError as e:
                error = str(e)

        return render_template("index.html", weather=weather, error=error)

    return app