import boto3
from boto3.dynamodb.conditions import Key
import datetime
import hashlib
import jwt
import json
import os

""" Class variant of the code """
class LoginService():

    SECRET = "IWillNotTellYou"
    ISSUER = "https://uc.no"
    AUDIENCE = "https://www.uc.no"

    def __init__(self, username, password) -> None:
        self._username = username
        self._password = password
        self._passwordvalidated = False
        self.user = None

    def getuser(self):
        table = boto3.resource('dynamodb').Table('users')
        response = table.query(KeyConditionExpression=Key('email').eq(self._username))
        self.user = response['Items'][0]

    def checkpassword(self):
        hashedpass = self.user['hashedpass'].value
        salt = hashedpass[:32] 
        key = hashedpass[32:]   

        new_key = hashlib.pbkdf2_hmac('sha256', self._password.encode('utf-8'), salt, 100000, dklen=128)

        if new_key == key:
            self._passwordvalidated = True
            return True        
            
        return self._passwordvalidated

    def createjwttoken(self):
        
        payload_data = {
            "name": self.user['fullname'],
            "email": self.user['email'],
            "iss": self.ISSUER,
            "aud": self.AUDIENCE,
            "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(seconds=10)
        }

        self._token = jwt.encode(
            payload=payload_data,
            key=self.SECRET,
            algorithm='HS256',    
        )

""" 
    **********************************
    Handler metoden som bruker klassen
    **********************************
"""
def lambda_handler(event, context):

    print (event)
    
    if event['rawPath'] == "/login":

        # Body kan være decoded base64
        payload = json.loads(event["body"])

        loginsw = LoginService(payload['userid'], payload['password'])
        loginsw.getuser()
        loginsw.checkpassword()
        if loginsw.checkpassword():
            loginsw.createjwttoken()

            return { 
                'token': loginsw._token
            }            
        
    # Returner uautorisert
    return { 'statusCode' : 401 }
