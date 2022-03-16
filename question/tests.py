from urllib import response
from django.test import TestCase
from utils.sort import sorting_answers
from utils.pagination import get_next_question
from question.models import Question

# Create your tests here.

class QuestionsTest(TestCase):

    def create_question(self, question_data):
        return Question.objects.create(
            text = question_data['text'],
            choice_a = question_data['choice_a'],
            choice_b = question_data['choice_b'],
            choice_c = question_data['choice_c'],
            choice_d = question_data['choice_d'],
            choice_e = question_data['choice_e'],
            correct_answer = question_data['correct_answer'],
        )

    def test_sorted_answers(self):
        mocked_answers = {
            'a': '0',
            'b': '2',
            'c': '16',
            'd': '32',
            'e': '128',
        }

        wrong_sort_answers = {
            'a': '0',
            'c': '16',
            'e': '128',
            'b': '2',
            'd': '32',
        }
        
        self.assertEqual(mocked_answers, sorting_answers(wrong_sort_answers))
    
    def test_next_question(self):
        question1 = self.create_question({
            'text': 'Quanto é 2+2?',
            'choice_a': '1',
            'choice_b': '2',
            'choice_c': '3',
            'choice_d': '4',
            'choice_e': '5',
            'correct_answer': 'd',
        })
        question2 = self.create_question({
            'text': 'Quanto é 2+3?',
            'choice_a': '1',
            'choice_b': '2',
            'choice_c': '3',
            'choice_d': '4',
            'choice_e': '5',
            'correct_answer': 'e',
        })
        self.assertEqual(question2.id, get_next_question(question1.id))
    
    def test_question_view(self):
        question = self.create_question({
            'text': 'Quanto é 2+2?',
            'choice_a': '1',
            'choice_b': '2',
            'choice_c': '3',
            'choice_d': '4',
            'choice_e': '5',
            'correct_answer': 'd',
        })
        index_view = self.client.get('/')
        self.assertEqual(index_view.status_code, 200)
        question_path = '/'+str(question.id)+'/'
        question_view = self.client.get(question_path)
        self.assertEqual(question_view.status_code, 200)

    def test_response_view(self):
        question = self.create_question({
            'text': 'Quanto é 2+2?',
            'choice_a': '1',
            'choice_b': '2',
            'choice_c': '3',
            'choice_d': '4',
            'choice_e': '5',
            'correct_answer': 'd',
        })
        wrong_answer = self.client.post('/resposta/', {'answer': 'b', 'question_id': str(question.id)})
        self.assertEqual(wrong_answer.status_code, 200)
        self.assertEqual(wrong_answer.context['is_correct'], False)

        correct_answer = self.client.post('/resposta/', {'answer': 'd', 'question_id': str(question.id)})
        self.assertEqual(correct_answer.status_code, 200)
        self.assertEqual(correct_answer.context['is_correct'], True)

