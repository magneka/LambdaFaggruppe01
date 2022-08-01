import pytest
import sys

# For å kjøre pystest
sys.path.append("/Users/magnealvheim/Documents/Source/AWS/LambdaFaggruppe/workdir")
import app

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
            "path": "/login",
        }

    @pytest.fixture
    def context(self):
        return None


    def test_lambda_handler(self, event, context):

        ret = app.handler(event, "")
        
        token = ret["body"]["token"]
        print ("Token:", token )
        
        assert (ret["body"]["token"] != "")
        assert ret["statusCode"] == 200

