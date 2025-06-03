import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Load system prompt from a file
with open("System.txt", "r", encoding="utf-8") as f:
    system_prompt = f.read()

# Get API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables.")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",

)

messages = [
    {"role": "system", "content": system_prompt} # system instruction
]

print("Chat with your  AI assistant (type 'exit' to quit)\n", flush=True)

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    messages.append({"role": "user", "content": user_input})

    print("Generating a response...\n", flush=True)
    response = client.chat.completions.create(
        model="deepseek/deepseek-r1:free",
        messages=messages
    )


    reply = response.choices[0].message.content.strip()

    print(f"FeedbackIQ: {reply}\n")

    messages.append({"role": "assistant", "content": reply})
