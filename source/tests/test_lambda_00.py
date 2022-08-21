import pytest
import sys

# For å kjøre pystest, legg til path til lambda
sys.path.append("/source/lambda00")
import lambda_function as app

# For å kjøre test fra vscode
#from workdir import app

class TestServiceHandler:

    @pytest.fixture
    def event(self):
        """ Generates API GW Event"""

        return {
            "body": '{}',           
            "requestContext": {},           
            "headers": { },
            "httpMethod": "GET",
            "rawPath": "",
        }

    @pytest.fixture
    def context(self):
        return None


    def test_lambda_handler(self, event, context):

        ret = app.lambda_handler(event, "")
               
        body = ret["body"]
        print ("Body:", body )
                
        assert (body == 'Hello from Lambda!')
        assert ret["statusCode"] == 200