from survey import AnonymousSurvey
import pytest

@pytest.fixture
def language_survey():
    question = "Jaki jest Twój ojczysty język?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    language_survey.store_response('polski')
    assert 'polski' in language_survey.responses

def test_store_three_response(language_survey):
    responses = ['angielski', 'hiszpański', 'polski']

    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses
    