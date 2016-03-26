"""
Creates a Codepipeline object to test events with
"""
import json
import pkg_resources

class Codepipeline(object):
    """
    Codepipeline sample events
    """
    def __init__(self):
        data_file = open(pkg_resources.resource_filename(
            "lambda_sample_events", "json_samples/codepipeline.json"))
        self.event = json.load(data_file)

    def make_invalid(self):
        """Removes the CodePipeline.job key to make the object unusable"""
        self.event.pop("CodePipeline.job", None)

    def change_function_name_to(self, name):
        """Change the name of the Lambda function in the event"""
        self.event['CodePipeline.job']['data']['actionConfiguration']\
            ['configuration']['FunctionName'] = str(name)
