import requests
from .config import API_KEY, BASE_URL

def fetch_weather(city: str) -> dict | None:
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    r = requests.get(BASE_URL, params=params, timeout=10)
    if r.status_code == 200:
        return r.json()
    return None

def parse_weather(data: dict) -> dict:
    if not data:
        raise ValueError("Aucune donnée météo reçue.")
    # OpenWeather peut renvoyer cod en int ou str selon cas
    if str(data.get("cod", "200")) != "200":
        msg = data.get("message", "ville inconnue")
        raise ValueError(f"Erreur OpenWeather: {msg}")

    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
    }