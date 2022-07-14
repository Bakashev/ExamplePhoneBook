class AnonymousSurvey():
    """the class collection answer on quistion"""
    def __init__(self,question):
        """Function save question and ready save answer"""
        self.question = question
        self.response = []

    def show_question(self):
        """Show question"""
        print(self.question)

    def store_response(self, new_response):
        """Save response"""
        self.response.append(new_response)
    def sho_rezult(self):

        print("Show response:")
        for rezult in self.response:
            print('Your question: {} \n Your answer: {}'.format(self.question,rezult))
