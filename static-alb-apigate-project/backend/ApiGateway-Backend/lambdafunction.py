import json

def lambda_handler(event, context):
    response = {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',  # Adjust this header based on your CORS requirements
        },
        'body': json.dumps({'message': 'Hello from Lambda!'}),
    }

    return response
