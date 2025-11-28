client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Modify the messages
messages.append({"role": "system", "content": "Don't make assumptions about what values to plug into functions."})

response = get_response(messages, function_definition)

print(response)