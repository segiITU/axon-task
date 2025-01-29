import streamlit as st
from src.weather_api import WeatherService
from src.llm_service import LLMService
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    st.title("Copenhagen Weather Assistant")
    
    # Default location (Copenhagen)
    lat = 55.6761
    lon = 12.5683
    
    weather_service = WeatherService()
    llm_service = LLMService()
    
    question = st.text_input("What's your weather question?")
    
    if st.button("Get Answer"):
        try:
            today = datetime.now().strftime("%Y-%m-%d")
            if "sunrise" in question.lower() or "sunset" in question.lower():
                weather_data = weather_service.get_sunrise_sunset(lat, lon, today)
            elif "temperature" in question.lower():
                weather_data = weather_service.get_temperature(lat, lon, today)
            else:
                st.error("Sorry, I can only answer questions about sunrise/sunset and temperature.")
                return
                
            response = llm_service.process_question(question, weather_data)
            st.write(response)
            
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()