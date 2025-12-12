
from google import genai
from google.genai import types
from decouple import config

GEMINI_API_KEY = config("GEMINI_API_KEY")
prompt = input("Enter a prompt:")

client = genai.Client(api_key=GEMINI_API_KEY)

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents= prompt,
    config=types.GenerateContentConfig(
        system_instruction="You name is alex and you always talk in a friendly tone , You should not think about sports ",
        temperature=0.2 #Creativity 0 - 2
    )
)

print(response.text)