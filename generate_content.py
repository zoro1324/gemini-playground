
from google import genai
from decouple import config

GEMINI_API_KEY = config("GEMINI_API_KEY")
prompt = ["Explain about AI in 400 words"]

client = genai.Client(api_key=GEMINI_API_KEY)

response = client.models.generate_content_stream(
    model="gemini-2.5-flash",
    contents= prompt
)

for i in response:
    print(i.text)