"""
Unit Tests for Codepipeline class
"""
import json
import pytest
from lambda_sample_events import SampleEvent
from lambda_sample_events.unknown_service_error import UnknownServiceError

JSON_SAMPLES = 'lambda_sample_events/json_samples/'

def test_invalid_service_name():
    """ Tests invoking with an invalid Service Name """
    with pytest.raises(UnknownServiceError):
        SampleEvent('invalid')

def test_codepipeline():
    """ Tests Codepipeline """
    codepipeline = SampleEvent('codepipeline')
    json_event = json.load(open(JSON_SAMPLES + 'codepipeline.json'))
    assert codepipeline.event == json_event

def test_sns():
    """ Tests SNS """
    codepipeline = SampleEvent('sns')
    json_event = json.load(open(JSON_SAMPLES + 'sns.json'))
    assert codepipeline.event == json_event
