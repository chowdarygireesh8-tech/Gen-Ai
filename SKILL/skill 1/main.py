
import os
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

# Create Gemini client
client = genai.Client(api_key=api_key)

print("Connecting to Google Gemini...")

# Send request using Interactions API
response = client.interactions.create(
    model="gemini-3.8-flash",
    input="What is Artificial Intelligence? Explain in simple words."
)

# Display response
print("\nLLM Response:")
print(response.output_text)

print("\nAPI call completed successfully!")
