import os
import google.generativeai as genai

# Fetch API key from the environment variable using the correct name
genai.configure(api_key=os.environ["GENERATIVE_AI_API_KEY"])
#make sure to set the GENERATIVE-API-KEY THROUGH COMMAND SHELL OR BASH
# Continue with the rest of your code...

# Generation configuration for the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Initialize the GenerativeModel with your configuration
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Start the chat session with initial conversation history
chat_session = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": ["Tell me about the impact of World War II and how it led to the independence of various nations"],
        },
        {
            "role": "model",
            "parts": [
                "Hey there, human! 👋 I'm here to help you with any information or spark creativity. 🚀 What's on your mind? Let's get started!"
            ],
        },
    ]
)

# Loop to continuously take queries from the user
print("Type 'exit' to quit.")
while True:
    # Take command or question input from the user
    input_text = input("Enter your question or command: ")
    
    # Exit the loop if the user types 'exit'
    if input_text.lower() == "exit":
        print("Exiting the chat. Goodbye!")
        break
    
    # Send the input text to the model and get a response
    response = chat_session.send_message(input_text)
    
    # Print the model's response
    print("AI:", response.text)
