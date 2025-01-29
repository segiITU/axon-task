from weather_api import WeatherService
from llm_service import LLMService
from datetime import datetime
import os

def main():
    # Default location (Copenhagen)
    lat = 55.6761
    lon = 12.5683

    # Initialize services
    weather_service = WeatherService()
    llm_service = LLMService()

    # Get user input
    question = input("What's your weather question? ")

    try:
        # Fetch weather data
        today = datetime.now().strftime("%Y-%m-%d")
        if "sunrise" in question.lower() or "sunset" in question.lower():
            weather_data = weather_service.get_sunrise_sunset(lat, lon, today)
        elif "temperature" in question.lower():
            weather_data = weather_service.get_temperature(lat, lon, today)
        else:
            print("Sorry, I can only answer questions about sunrise/sunset and temperature.")
            return

        # Generate and print response
        response = llm_service.process_question(question, weather_data)
        print(response)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()