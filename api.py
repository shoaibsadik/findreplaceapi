import json

def replace_words(input_str):
    # Define the find and replace mappings
    word_replacements = {
        "Google": "Google©"
        # Add more replacements as needed
    }

    # Perform find and replace
    for word, replacement in word_replacements.items():
        input_str = input_str.replace(word, replacement)

    return input_str

def lambda_handler(event, context):
    try:
        # Extract the input string from the API request
        input_str = event['queryStringParameters']['input']

        # Perform the find and replace operation
        result = replace_words(input_str)

        # Return the modified string as a JSON response
        return {
            'statusCode': 200,
            'body': json.dumps({'output': result})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
