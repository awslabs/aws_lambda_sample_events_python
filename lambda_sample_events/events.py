import json
import pkg_resources

def codepipeline():
    with open(pkg_resources.resource_filename(
        "lambda_sample_events",
        "json_samples/codepipeline.json"
    )) as data_file:
        return json.load(data_file)
