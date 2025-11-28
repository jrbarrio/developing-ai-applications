client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Append the second function
function_definition.append({'type': 'function', 'function':{'name': 'reply_to_review', 'description': 'Reply politely to the customer who wrote the review', 'parameters': {'type': 'object', 'properties': {'reply': {'type': 'string','description': 'Reply to post in response to the review'}}}}})

response = get_response(messages, function_definition)

# Print the response
print(response)