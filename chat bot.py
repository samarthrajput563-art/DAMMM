import os
import sys
try:
    import google.generativeai as genai
except ImportError:
    print(" :+!! Error: google-generativeai package is not installed. Install it with `pip install google-generativeai`.")
    sys.exit(1)
from dotenv import load_dotenv

load_dotenv(override=True)

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    print(":-!! Error: GEMINI_API_KEY not found in .env file")
    sys.exit(1)

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")  # or "gemini-1.5-pro" for more power

conversation_history = []
chat = model.start_chat(history=conversation_history)

print(":- Gemini Chatbot Ready!")
print("   Type 'exit' to quit, 'clear' to reset conversation.")
print("-" * 50)


def get_gemini_response(user_input: str) -> str:
    """Send a message using the persistent chat session and return response."""
    try:
        response = chat.send_message(user_input)
        return getattr(response, "text", str(response))
    except Exception as e:
        return f"!!! Error: {str(e)}"


while True:
    user_input = input("\nYou: ").strip()

    if user_input.lower() == "exit":
        print("Goodbye! Have a Great Day!....")
        break
    elif user_input.lower() == "clear":
        conversation_history = []
        chat = model.start_chat(history=conversation_history)
        print(":- Conversation history cleared.")
        continue

    elif not user_input:
        print("Please type something.")
        continue

    print("Bot: ", end="", flush=True)
    reply = get_gemini_response(user_input)
    print(reply)

