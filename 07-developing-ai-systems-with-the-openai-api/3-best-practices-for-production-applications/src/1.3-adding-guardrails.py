client = OpenAI(api_key="<OPENAI_API_TOKEN>")

user_request = "Can you recommend a good restaurant in Berlin?"

# Write the system and user message
messages = [{
    "role": "system",
    "content": "Provide advice for tourists visiting Rome. Keep the topics limited to only covering questions about food and drink, attractions, history and things to do around the city. For any other topic, apologize and say 'Apologies, but I am not allowed to discuss this topic.'.",
}, {
    "role": "user", 
    "content": user_request
},]

response = client.chat.completions.create(
    model="gpt-4o-mini", messages=messages
)

# Print the response
print(response.choices[0].message.content)