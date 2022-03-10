from django.test import TestCase
from utils.sort import sorting_answers

# Create your tests here.

class QuestionsTest(TestCase):

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