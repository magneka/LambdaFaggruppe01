import boto3
from boto3.dynamodb.conditions import Key

def getuser(email):
    table = boto3.resource('dynamodb').Table('users')
    response = table.query(KeyConditionExpression=Key('email').eq(email))
    result = response['Items'][0]
    return result


def handler(event, context):

    user = getuser('paula99@example.com')
   
    return {
        'statusCode': 200,
        'body': {
            'user': user['fullname']
        }
    }
        

hres = handler (None, None)
print (hres)


