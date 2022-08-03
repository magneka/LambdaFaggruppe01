# Første versjon, henter brukerdata fra dynamodb
import boto3
from boto3.dynamodb.conditions import Key

def getuser(email):
    table = boto3.resource('dynamodb').Table('users')
    response = table.query(KeyConditionExpression=Key('email').eq(email))
    result = response['Items'][0]
    return result


def  lambda_handler(event, context):

    user = getuser('paula99@example.com')
   
    return {
        'statusCode': 200,
        'body': {
            'user': user['fullname']
        }
    }
        

