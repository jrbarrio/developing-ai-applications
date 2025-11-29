client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the function to pass to tools
function_definition = [
    {
        "type": "function",
        "function": {
            "name": "get_airport_info",
            "description": "Get information for a specific airport",
            "parameters": {
                "type": "object",
                "properties": {
                    "airport_code": {
                        "type": "string",
                        "description": "The airport code to be passed to the get_airport_info function",
                    }
                },
            },
            "result": {"type": "string"},
        },
    }
]

response = get_response(function_definition)
print(response)
