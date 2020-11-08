from django.test import TestCase
from .models import Question

# Create your tests here.
class QuestionTestCase(TestCase):

    __question = None
    __text = 'Quanto é 2^5?'
    __answers = {
        'b': '2',
        'a': '0',
        'c': '16',
        'e': '128',
        'd': '32',
    }

    def setUp(self):

        self.__question = Question.objects.create(title=self.__text)

        for answer in self.__answers:
            self.__question.add_answer(answer, self.__answers[answer])

    def test_sorted_answers(self):
        self.assertEqual(list(Question.objects.last().get_answers().keys()), list(sorted(self.__answers.keys())))






