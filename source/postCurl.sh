#!/bin/bash
curl -X GET \
    'https://55rpnckaulh5xfdeo64vdrih4y0syiqk.lambda-url.eu-west-1.on.aws/' 

sleep 15
aws logs tail  /aws/lambda/ucpython

#aws lambda invoke --function-name my-function --cli-binary-format raw-in-base64-out --payload '{"key": "value"}' out
#sed -i'' -e 's/"//g' out
#sleep 15
#aws logs get-log-events --log-group-name /aws/lambda/ucpython --log-stream-name --limit 5