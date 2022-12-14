import boto3
from boto3.dynamodb.conditions import Key
import datetime
import hashlib
import jwt
import json
import os
import uuid

def createUserHash(userName, userEmail, userPass):
    salt = os.urandom(32) # Remember this

    key = hashlib.pbkdf2_hmac(
        'sha256', # The hash digest algorithm for HMAC
        userPass.encode('utf-8'), # Convert the password to bytes
        salt, # Provide the salt
        100000, # It is recommended to use at least 100,000 iterations of SHA-256 
        dklen=128 # Get a 128 byte key
    )

    hash = salt + key 

    item = {
        'email':      userEmail,
        'fullname':   userName,
        'hashedpass': salt + key,
        'password':   userPass
    }
    print(item)
    return item

def writeUserToDatabase(userRecord):
    TABLE_NAME = "users"

    # Creating the DynamoDB Client
    dynamodb_client = boto3.client('dynamodb', region_name="eu-west-1")

    # Creating the DynamoDB Table Resource
    dynamodb = boto3.resource('dynamodb', region_name="eu-west-1")
    table = dynamodb.Table(TABLE_NAME)

    item = createUserHash()
    response = table.put_item(
        TableName=TABLE_NAME, 
        Item=item
    )

def getuser(email):
    table = boto3.resource('dynamodb').Table('users')
    response = table.query(KeyConditionExpression=Key('email').eq(email))
    result = response['Items'][0]
    #print(result)
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

def lambda_handler(event, context):
    
    print (event)
    
    if event['rawPath'] == "/login":
        
        # Body kan v??re decoded base64
        decodedEvent = json.loads(event['body'])
        userid =  decodedEvent['userid']
        password =  decodedEvent['password']
        
        user = getuser(userid)

        validated = checkpassword(user, password)
        
        token = None
        if (validated):
            token = createjwttoken(user)
        
            return { 
                'token': token
            }
    
    # Kommer du hit, er du ikke logget p??        
    return { 
        'statusCode' : 401 
    }
    