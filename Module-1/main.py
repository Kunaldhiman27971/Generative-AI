from google import genai # ye package is not available in pip, you can install it using pip install google-genai
from dotenv import load_dotenv # type: ignore
import os # iska use hum environment variable ko access karne ke liye karte hai

load_dotenv() # ye function .env file ko load karne ke liye use hota hai, jisse hum apne environment variables ko access kar sake

client=genai.Client(api_key=os.getenv("GEMINI_API_KEY")) # ye line humare GEMINI_API_KEY ko environment variable se access kar rahi hai aur usse genai client me use kar rahi hai

response=client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Write a detailed explanation on how to improve bifacial gain in solar panels."
) # is code me humne genai client ka use karke ek model ko call kiya hai jo hume content generate karke dega. Humne model ka naam "gemini-2.5-flash" diya hai aur contents me humne ek prompt diya hai jisme humne poocha hai ki solar panels me bifacial gain ko kaise improve kiya ja sakta hai.

print(response.text) # ye line humare response ka text print kar rahi hai jo hume model se mila hai.
