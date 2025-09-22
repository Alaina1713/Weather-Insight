import requests

API_KEY = "YOUR_OPENWEATHERMAP_KEY"  # Replace with your free OpenWeatherMap API key

def get_weather(city):
    """
    Fetch weather data for a given city.
    Returns a dictionary with city, temp, condition, humidity, wind.
    Returns None if city not found or API fails.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()
        return {
            "city": city,
            "temp": data["main"]["temp"],
            "condition": data["weather"][0]["description"].title(),
            "humidity": data["main"]["humidity"],
            "wind": data["wind"]["speed"]
        }
    except:
        return None
