client = OpenAI(api_key="<OPENAI_API_TOKEN>")

messages = []
# Provide a system message and user messages to send the batch
messages.append({"role": "system", "content": """You are given a series of measurements in kilometers and are asked to return those values converted to miles. Provide the results in a table."""})
# Append measurements to the message
[messages.append({"role": "user", "content": str(i) }) for i in measurements]

response = get_response(messages)
print(response)