[![Coverage Status](https://coveralls.io/repos/github/irlrobot/python_lambda_sample_events/badge.svg?branch=master)](https://coveralls.io/github/irlrobot/python_lambda_sample_events?branch=master)
[ ![Codeship Status for irlrobot/python_lambda_sample_events](https://codeship.com/projects/938444a0-d5be-0133-1313-7edf9ccff8c4/status?branch=master)](https://codeship.com/projects/142651)
# Python module for creating sample events to test AWS Lambda functions.

# Usage

## Codepipeline
### Create a standard Codepipeline event
```python
import lambda_sample_events
from pprint import pprint
codepipeline = lambda_sample_events.Codepipeline()
pprint(codepipeline.event)
```
