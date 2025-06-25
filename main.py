import os
from dotenv import load_dotenv
import sys
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)

user_prompt = sys.argv

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt[1])]),
]


if len(user_prompt) >= 2:
    response = client.models.generate_content(model = "gemini-2.0-flash-001",
                                          contents = messages
                                          )
else:
    print("No prompt was provided")
    sys.exit(1)

print(response.text)

if len(user_prompt) == 3 and user_prompt[2] == "--verbose":
    print(f"User prompt: {user_prompt[1]}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")