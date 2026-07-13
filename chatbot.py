import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def ask_ai(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",   # You can also try "gemini-flash-latest"
            contents=prompt
        )
        return response.text

    except Exception as e:
        return f"ERROR:\n{e}"