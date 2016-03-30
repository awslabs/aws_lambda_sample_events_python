"""
The module will generate an "event" that appears to come from a specified
service which can be used to simulate an actual invocation of a Lambda function.
"""
import json
import pkg_resources
from aws_lambda_sample_events.unknown_service_error import UnknownServiceError

SERVICES = [
    'codepipeline',
    'sns',
    'cloudformation',
    'ses',
    'scheduled',
    'dynamodb_update',
    'cognito_sync_trigger',
    'kinesis_stream',
    's3_put',
    's3_delete',
    'cloudwatch_logs',
    'cloudwatch_events',
    'config_rule'
]

class SampleEvent(object):
    """
    Generates a sample event for the given service name

    Args:
        service_name (str): The name of a supported service.  See README.md.

    Attributes:
        event (str): Returns a JSON event for the specified service.

    Raises:
        UnknownServiceError: An unsupported service name was used.  See README.md.
    """
    def __init__(self, service_name):
        self.event = SampleEvent.load_event(service_name)

    @staticmethod
    def load_event(service_name):
        """ Loads a sample JSON event for the specified service """
        SampleEvent.validate_service_name(service_name)
        filename = 'json_samples/' + service_name + '.json'
        data_file = open(pkg_resources.resource_filename(
            "aws_lambda_sample_events", filename))
        return json.load(data_file)

    @staticmethod
    def validate_service_name(service_name):
        """ Validates the specified service name is supported """
        if not service_name in SERVICES:
            raise UnknownServiceError('Valid Services are: ' + str(SERVICES))
