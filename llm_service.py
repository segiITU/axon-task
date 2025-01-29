from openai import OpenAI

class LLMService:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("API key required")
        self.client = OpenAI(api_key=api_key)

    def process_question(self, question, weather_data):
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