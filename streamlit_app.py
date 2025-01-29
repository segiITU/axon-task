import streamlit as st
from weather_api import WeatherService
from llm_service import LLMService
from datetime import datetime

def main():
    st.title("Copenhagen Weather Assistant")
    
    # Default location set to Copenhagen
    lat = 55.6761
    lon = 12.5683
    
    api_key = st.secrets["OPENAI_API_KEY"]
    
    weather_service = WeatherService()
    llm_service = LLMService(api_key)
    
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