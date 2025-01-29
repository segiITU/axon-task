import requests

def get_weather_forecast(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max&timezone=auto"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["daily"]["temperature_2m_max"][0]  # Temperature for tomorrow
    else:
        return None

def is_cold(temperature, cold_threshold=10):
    return temperature < cold_threshold

def main():
    latitude = 55.6761
    longitude = 12.5683

    temperature = get_weather_forecast(latitude, longitude)
    if temperature is not None:
        # Check if it will be cold
        if is_cold(temperature):
            print("Yes, it will be cold tomorrow.")
        else:
            print("No, it won't be cold tomorrow.")
    else:
        print("Failed to fetch weather data.")

# Run the program
if __name__ == "__main__":
    main()