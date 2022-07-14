import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for class AnonymnousSurvey"""
    def setUp(self):
        question = 'What is your name'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Sergey', 'Alina', 'Dasha']

    def test_store_single_response(self):
        """One response save try"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.response)

    def test_store_three_response(self):
        """Three response save true"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.my_survey.response:
            self.assertIn(response, self.my_survey.response)

