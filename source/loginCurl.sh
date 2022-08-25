#!/bin/bash
curl -X POST \
    'https://9s9hsi4o62.execute-api.eu-west-1.amazonaws.com/login' \
    -H 'Content-Type: application/json' \
    -d "@payload.json"
 

sleep 15
aws logs tail  /aws/lambda/ucpython

#aws lambda invoke --function-name my-function --cli-binary-format raw-in-base64-out --payload '{"key": "value"}' out
#sed -i'' -e 's/"//g' out
#sleep 15
#aws logs get-log-events --log-group-name /aws/lambda/ucpython --log-stream-name --limit 5