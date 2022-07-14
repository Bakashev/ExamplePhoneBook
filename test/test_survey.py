import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for class AnonymnousSurvey"""
    def test_store_single_response(self):
        """One response save try"""
        question = 'What is your name'
        my_survey=AnonymousSurvey(question)
        my_survey.store_response('Sergey')
        self.assertIn('Sergey',my_survey.response)

    def test_store_three_response(self):
        """Three response save true"""
        qustion = 'What is your name and names your family'
        my_survey = AnonymousSurvey(qustion)
        responses = ['Sergey','Alina','Dasha']
        for response in responses:
            my_survey.store_response(response)
        for response in my_survey.response:
            self.assertIn(response, my_survey.response)

