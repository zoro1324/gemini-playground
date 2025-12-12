
from google import genai
from decouple import config

GEMINI_API_KEY = config("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

print("NOTE: Enter exit to end chat")

while True:
    print("="*100)
    user_input = input("User : ")

    if (user_input.lower()=="exit") :
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents = user_input
    )

    print("AI:",response.text)