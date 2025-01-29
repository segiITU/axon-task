import requests

class WeatherService:
    def get_sunrise_sunset(self, lat, lon, date):
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=sunrise,sunset&timezone=auto"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return {
                "sunrise": data["daily"]["sunrise"][0],
                "sunset": data["daily"]["sunset"][0]
            }
        return None
        
    def get_temperature(self, lat, lon, date):
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max&timezone=auto"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data["daily"]["temperature_2m_max"][0]
        return None