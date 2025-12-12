
from google import genai
from decouple import config

GEMINI_API_KEY = config("GEMINI_API_KEY")
prompt = input("Enter a prompt:")

client = genai.Client(api_key=GEMINI_API_KEY)

response = client.models.generate_content_stream(
    model="gemini-2.5-flash",
    contents= prompt
)

for chunk in response:
    print(chunk.text)