import pytest

from workdir import app

class TestServiceHandler:

    @pytest.fixture
    def event(self):
        """ Generates API GW Event"""

        return {
            "body": '{ "test": "body"}',           
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

