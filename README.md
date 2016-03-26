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
