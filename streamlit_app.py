import streamlit as st
from weather_api import WeatherService
from llm_service import LLMService
from datetime import datetime

def main():
    st.title("Copenhagen Weather Assistant")
    
    try:
        api_key = st.secrets["OPENAI_API_KEY"]
        lat = 55.6761  # Copenhagen
        lon = 12.5683
        
        weather_service = WeatherService()
        llm_service = LLMService(api_key)
        
        question = st.text_input("What's your weather question?")
        
        if st.button("Get Answer"):
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
            
    except KeyError:
        st.error("OpenAI API key not found in secrets")
    except Exception as e:
        st.error(f"Error: {e}")

if __name__ == "__main__":
    main()