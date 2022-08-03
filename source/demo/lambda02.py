import boto3
from boto3.dynamodb.conditions import Key
import hashlib

def getuser(email):
    table = boto3.resource('dynamodb').Table('users')
    response = table.query(KeyConditionExpression=Key('email').eq(email))
    result = response['Items'][0]
    return result

def checkpassword(user, password):
    hashedpass = user['hashedpass'].value
    salt = hashedpass[:32] 
    key = hashedpass[32:]   

    new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000, dklen=128)

    if new_key == key:
        return True
    else:
        return False


def handler(event, context):

    user = getuser('paula99@example.com')
    password = 'wy3mSZ1y@9'

    validated = checkpassword(user, password)
   
    return {
        'statusCode': 200,
        'body': {
            'user': user['fullname'],
            'validpassword': validated
        }
    }
        
hres = handler (None, None)
print (hres)