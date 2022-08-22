'''

curl -X GET \
    'https://55rpnckaulh5xfdeo64vdrih4y0syiqk.lambda-url.eu-west-1.on.aws' \
    -H 'Content-Type: application/json'    

curl -X POST \
    'https://55rpnckaulh5xfdeo64vdrih4y0syiqk.lambda-url.eu-west-1.on.aws/login' \
    -H 'Content-Type: application/json' \
    -d '"userid": "aula99@example.com", "password":"wy3mSZ1y@9"'


curl -X POST \
    'https://9s9hsi4o62.execute-api.eu-west-1.amazonaws.com/login' \
    -H 'Content-Type: application/json' \
    -d '"userid": "aula99@example.com", "password":"wy3mSZ1y@9"'

'''

# importing the requests library
import requests
  
# defining the api-endpoint 
API_ENDPOINT = "https://55rpnckaulh5xfdeo64vdrih4y0syiqk.lambda-url.eu-west-1.on.aws/login"
 
 
# data to be sent to api
data = {'userid': 'aula99@example.com',
        'password':'wy3mSZ1y@9'}
  
# sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, data = data)
  
# extracting response text 
pastebin_url = r.text
print("The pastebin URL is:%s"%pastebin_url)