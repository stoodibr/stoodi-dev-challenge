from django.test import TestCase
from .models import Question, Alternatives

# Tests
class TestViewQuestion(TestCase):
    
    # Test response access
    def test_response_access_views(self):
        # Test Question Response
        response_question = self.client.get('')
        self.assertEqual(
            200,
            response_question.status_code
        )
        
        # Test Incorrect Answer
        response_answer = self.client.post('/resposta/', {'answer': 'a'})
        self.assertEqual(response_answer.status_code, 200)
        self.assertEqual(
            False,
            response_answer.context["is_correct"]
        )
        
        # Test Correct Answer
        response_answer = self.client.post('/resposta/', {'answer': 'd'})
        self.assertEqual(response_answer.status_code, 200)
        self.assertEqual(
            True,
            response_answer.context["is_correct"]
        )
    
    # Test answers ordering feature
    def test_answer_order_feature(self):
        response_question = self.client.get('')
        
        question = Question(
            question_text = 'Quanto é 2^5?'
        )
        
        alternatives = Alternatives(
            question_text = 'Quanto é 2^5?'
        )
        
        # Test if the keys are in order
        self.assertEqual(
            ["a", "b", "c", "d", "e"],
            list(response_question.context["questions"][0].keys())
        )