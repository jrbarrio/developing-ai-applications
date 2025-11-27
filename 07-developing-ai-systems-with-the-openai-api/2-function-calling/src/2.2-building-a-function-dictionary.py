client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the function parameter type
function_definition[0]['function']['parameters']['type'] = 'object'

# Define the function properties
function_definition[0]['function']['parameters']['properties'] = {
    'title': {'type': 'string', 'description': 'Title'}, 
    'year': {'type': 'string', 'description': 'Publication year'}, 
}

response = get_response(messages, function_definition)
print(response)