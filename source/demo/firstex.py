import boto3
from boto3.dynamodb.conditions import Key
import datetime
import hashlib
import jwt
import json
import os

def getuser(email):
    table = boto3.resource('dynamodb').Table('users')
    response = table.query(KeyConditionExpression=Key('email').eq(email))
    result = response['Items'][0]
    #print(result)
    return result

def lambda_handler(event, context):
    # TODO implement.
    getuser("paula99@example.com")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
