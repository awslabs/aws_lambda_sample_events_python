"""
Unit Tests for Codepipeline class
"""
from lambda_sample_events.codepipeline import Codepipeline

def test_make_invalid():
    """Tests the make_invalid function"""
    codepipeline = Codepipeline()
    codepipeline.make_invalid()
    assert codepipeline.event == {}

def test_change_function_name_to():
    """Tests the change_function_name_to function"""
    new_name = 'BLAH'
    codepipeline = Codepipeline()
    codepipeline.change_function_name_to(new_name)
    assert codepipeline.event['CodePipeline.job']['data']\
        ['actionConfiguration']['configuration']['FunctionName'] == new_name

def test_change_function_name_to_with_int():
    """Tests the change_function_name_to function with a non-string arg"""
    new_name = 1212121212
    codepipeline = Codepipeline()
    codepipeline.change_function_name_to(new_name)
    assert codepipeline.event['CodePipeline.job']['data']\
        ['actionConfiguration']['configuration']['FunctionName'] == str(new_name)
