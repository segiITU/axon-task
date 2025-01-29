from openai import OpenAI
import os

class LLMService:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    def process_weather_question(self, temperature):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful weather assistant. Provide concise, natural responses about weather conditions."},
                {"role": "user", "content": f"The forecast temperature for tomorrow is {temperature}°C. Is it going to be cold? Respond conversationally in one sentence."}
            ]
        )
        return response.choices[0].message.content

def main():
    llm = LLMService()
    response = llm.process_weather_question(5)
    print(response)

if __name__ == "__main__":
    main()