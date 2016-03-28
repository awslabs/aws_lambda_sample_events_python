"""
Generates a sample event for the given service name
"""
import json
import pkg_resources
from unknown_service_error import UnknownServiceError

SERVICES = 'codepipeline'

class SampleEvent(object):
    """
    Client for sample events
    """
    def __init__(self, service_name):
        try:
            self.event = getattr(SampleEvent, service_name)()
        except AttributeError:
            raise UnknownServiceError('Valid Services are: ' + SERVICES)

    @staticmethod
    def codepipeline():
        """ Loads Codepipeline sample JSON event """
        data_file = open(pkg_resources.resource_filename(
            "lambda_sample_events", "json_samples/codepipeline.json"))
        return json.load(data_file)
