import os
from dotenv import load_dotenv
from mistralai.client import Mistral  

load_dotenv()


client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))

messages = []

while True:
    user_input = input("User: ")
    
    if user_input=="exit":
        break
    messages.append({
        "role": "user",
        "content": user_input,
    })
    response = client.chat.complete(
            model="mistral-large-latest",  # Use a valid model string
            messages=messages, 
        )
    ai_response = response.choices[0].message.content
    print("AI:", ai_response)
        
    # 3. Save the response back to history using the correct valid role: "assistant"
    messages.append({
            "role": "assistant",
            "content": ai_response,
        })