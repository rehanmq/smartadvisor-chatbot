# backend/generative_ai.py

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful customer support assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error generating response: {str(e)}"
