from collections import OrderedDict

from django.test import Client, TestCase
from .models import Question


# Create your tests here.
class QuestionTestCase(TestCase):

    __client = None

    def setUp(self):
        self.__client = Client()

    def create_a_question(self):
        title = 'Quanto é 2^5?'
        question = Question.objects.create(title=title)

        answers = {
            'b': '2',
            'a': '0',
            'c': '16',
            'e': '128',
            'd': '32',
        }

        for answer in answers:
            question.add_answer(answer, answers[answer])

        return question, title, answers

    def create_another_question(self):
        title = 'Qual a raiz quadrada de 64'
        question = Question.objects.create(title=title)

        answers = {
            'a': '1',
            'b': '2',
            'c': '4',
            'd': '8',
            'e': '16',
        }

        for answer in answers:
            question.add_answer(answer, answers[answer])

        return question, title, answers

    def test_sorted_answers(self):
        """verifica se alternativas estão ordenadas."""
        _, _, answers = self.create_a_question()

        self.assertEqual(list(Question.objects.last().get_answers().keys()), list(sorted(answers.keys())))

    def test_create_question(self):
        """verifica a criação de uma questão no banco."""
        question, title, answers = self.create_a_question()

        self.assertEqual(question.title, title)
        self.assertDictEqual(question.get_answers(), OrderedDict(sorted(answers.items())))

        question.set_correct_answer('d')

        self.assertEqual(question.correct_answer.letter, 'd')
        self.assertDictEqual(question.to_dict(), {
            'id': question.id,
            'title': title,
            'answers': OrderedDict(sorted(answers.items())),
            'correct_answer': 'd'
        })

    def test_no_question(self):
        """verifica resposta quando não há questões cadastradas no banco"""

        response = self.__client.get('/')

        self.assertTemplateUsed(response, 'question/no_question.html')

    def test_question(self):
        """verifica resposta requisição sem parâmetros."""
        question, _, _ = self.create_a_question()
        question.set_correct_answer('d')

        another_question, _, _ = self.create_another_question()
        another_question.set_correct_answer('d')

        response = self.__client.get('/')

        self.assertEqual(response.context['question']['id'], question.id)
        self.assertEqual(response.context['question']['title'], question.title)

        answers = question.get_answers()
        for letter, answer in response.context['question']['answers'].items():
            self.assertEqual(answer, answers[letter])

    def test_correct_answer(self):
        """caso em que resposta para questão está correta."""
        question, _, _ = self.create_a_question()
        question.set_correct_answer(letter='d')

        response = self.__client.get('/')
        previous = response.context['question']['id']

        response = self.__client.post(
            '/resposta/',
            {
                'answer': 'd',
                'current_question': previous
            }
        )

        self.assertEqual(response.context['is_correct'], True)
        self.assertEqual(response.context['previous_question'], str(previous))

    def test_wrong_answer(self):
        """caso em que resposta para questão está incorreta."""
        question, _, _ = self.create_a_question()
        question.set_correct_answer(letter='d')

        response = self.__client.get('/')
        previous = response.context['question']['id']

        response = self.__client.post(
            '/resposta/',
            {
                'answer': 'a',
                'current_question': previous
            }
        )

        self.assertEqual(response.context['is_correct'], False)
        self.assertEqual(response.context['previous_question'], str(previous))
