
class AnonymousSurvey:
    def __init__(self, question: str):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self, new_respons: str):
        self.responses.append(new_respons)

    def show_result(self):
        print("Oto wyniki ankiety:")
        for response in self.responses:
            print(f"-{response}")