import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table('resumes')

def handler(event, context):
    resume_id = event.get("pathParameters", {}).get("id", "123")

    response = table.get_item(Key={"id": resume_id})

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(response.get("Item", {}))
    }