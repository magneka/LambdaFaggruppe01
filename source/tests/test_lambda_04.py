import pytest
import sys

# For å kjøre pystest, legg til path til lambda
sys.path.append("/source/lambda04")
import lambda_function as app

# For å kjøre test fra vscode
#from workdir import app

class TestServiceHandler:

    @pytest.fixture
    def event(self):
        """ Generates API GW Event"""

        return {
            "body": '{ "userid": "paula99@example.com", "password": "wy3mSZ1y@9"}',           
            "requestContext": {},           
            "headers": { },
            "httpMethod": "POST",
            "rawPath": "/login",
        }

    @pytest.fixture
    def context(self):
        return None


    def test_lambda_handler(self, event, context):

        ret = app.lambda_handler(event, "")
        
        token = ret["token"]
        print ("Token:", token )
        
        assert (ret["token"] != "")
        #assert ret["statusCode"] == 200

