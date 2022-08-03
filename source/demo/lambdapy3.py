import boto3
from boto3.dynamodb.conditions import Key
import hashlib
import datetime
import jwt

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

def createjwttoken(user):
    secret = "IWillNotTellYou"
    issuer = "https://uc.no"
    audience = "https://www.uc.no"

    payload_data = {
        "name": user['fullname'],
        "email": user['email'],
        "iss": issuer,
        "aud": audience,
        "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(seconds=10)
    }

    token = jwt.encode(
        payload=payload_data,
        key=secret,
        algorithm='HS256',    
    )
    return token


def handler(event, context):

    user = getuser('paula99@example.com')
    password = 'wy3mSZ1y@9'

    validated = checkpassword(user, password)
    token = ''
    if (validated):
            token = createjwttoken(user)
   
    return {
        'statusCode': 200,
        'body': {
            'user': user['fullname'],
            'validpassword': validated,
            'token': token
        }
    }
        
hres = handler (None, None)
print (hres)