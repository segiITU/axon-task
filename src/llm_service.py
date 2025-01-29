from openai import OpenAI
import os

class LLMService:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def process_question(self, question, weather_data):
        """Generate a response using OpenAI's API."""
        prompt = f"""
        You are a weather assistant. The user asked: "{question}".
        Here is the relevant weather data: {weather_data}.
        Provide a helpful and conversational response.
        """
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful weather assistant."},
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content