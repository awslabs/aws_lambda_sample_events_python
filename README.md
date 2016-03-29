[![Coverage Status](https://coveralls.io/repos/github/irlrobot/python_lambda_sample_events/badge.svg?branch=master)](https://coveralls.io/github/irlrobot/python_lambda_sample_events?branch=master)
[ ![Codeship Status for irlrobot/python_lambda_sample_events](https://codeship.com/projects/938444a0-d5be-0133-1313-7edf9ccff8c4/status?branch=master)](https://codeship.com/projects/142651)
# Python module for creating sample events to test AWS Lambda functions.
This small module is meant to help test Python based [AWS Lambda](https://aws.amazon.com/lambda/) functions that get triggered by other AWS services (ex: CodePipeline action).  The module will generate an "event" that appears to come from a specified service which can be used to simulate an actual invocation of the function.

# Usage Example
```python
from lambda_sample_events import SampleEvent
from pprint import pprint
codepipeline = SampleEvent('codepipeline')
pprint(codepipeline.event)
```
`SampleEvent()` expects a single string argument representing the name of the AWS Service you would like a sample event for.  

## Valid arguments, and supported services, are:
* codepipeline
* sns
* cloudformation
* ses
* scheduled
* dynamodb_update
* cognito_sync_trigger
* kinesis_stream
* s3_put
* s3_delete
* cloudwatch_logs

# References
[AWS Lambda Event Sources](http://docs.aws.amazon.com/lambda/latest/dg/eventsources.html)

[AWS ARNs](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html)
