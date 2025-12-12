from google import genai
from decouple import config

GEMINI_API_KEY = config("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

chat = client.chats.create(model="gemini-2.0-flash-lite",)

print("NOTE: Enter exit to end chat")

while True:
    print("="*100)
    user_input = input("User : ")

    if (user_input.lower()=="exit") :
        break

    response = chat.send_message_stream(user_input)

    for chunk in response:
        print(chunk.text)


print("="*100)
print("Chat History:")
print("="*100)

for i in chat.get_history():
    print(f"{i.role} - {i.parts}")