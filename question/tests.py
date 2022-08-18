from django.test import TestCase
from .models import Question, Alternatives, QuestionLogs

# Tests
class TestViewQuestion(TestCase):
    
    # Test home access
    def test_home_view(self):
        # Test Question Response
        response_question = self.client.get('')
        self.assertEqual(
            200,
            response_question.status_code
        )
        
    # Test question access
    def test_question_view(self):
        
        # Question 1
        question1 = Question.objects.create(
                id = 1,
                question_text = "Quanto é 1 + 1?"
        )
        
        # Test Question Response with id error
        response_question = self.client.get('/2/')
        self.assertEqual(
            404,
            response_question.status_code
        )
        
        # Test Question Response
        response_question = self.client.get('/1/')
        self.assertEqual(
            200,
            response_question.status_code
        )
        
        # Test the return of the question object
        self.assertEqual(
            question1,
            response_question.context["questions"]['question_complete']
        )
        
        # Test the return of the question text
        self.assertEqual(
            "Quanto é 1 + 1?",
            response_question.context["questions"]['question'],
        )
        
        # Test the feedback if you have no alternatives for this question
        self.assertEqual(
            0,
            response_question.context["questions"]['alternatives'].count(),
        )
        
        alternative1 = Alternatives.objects.create(
            alternative_order = 'a',
            question = question1,
            alternative_text = "2",
            is_correct = True
        )
        
        alternative2 = Alternatives.objects.create(
            alternative_order = 'b',
            question = question1,
            alternative_text = "10",
            is_correct = False
        )
        
        response_question = self.client.get('/1/')
        # Test the feedback if you have one or more alternatives for this question
        self.assertEqual(
            2,
            response_question.context["questions"]['alternatives'].count(),
        )
        
    # Test anser access
    def test_answer_view(self):
        question1 = Question.objects.create(
                id = 1,
                question_text = "Quanto é 1 + 1?"
        )
        
        alternative1 = Alternatives.objects.create(
            alternative_order = 'a',
            question = question1,
            alternative_text = "2",
            is_correct = True
        )
        
        alternative2 = Alternatives.objects.create(
            alternative_order = 'b',
            question = question1,
            alternative_text = "10",
            is_correct = False
        )
        
        response_answer = self.client.post(
            '/resposta/', 
            {'answer': alternative1.id}
        )
        
        # Testar se deu certo o acesso
        self.assertEqual(
            200,
            response_answer.status_code
        )
        
        # Testar se a respostar está correta
        self.assertEqual(
            True,
            response_answer.context["is_correct"]
        )
    
        # Testar se foi gerado o log
        self.assertEqual(
            True,
            response_answer.context["is_correct"]
        )
        
        # Testar um acesso errado a url
        response_answer = self.client.post(
            '/resposta/123', 
            {'answer': 'a'}
        )
        
        self.assertEqual(
            404,
            response_answer.status_code
        )
        
        # Testar uma resposta errada
        response_answer = self.client.post(
            '/resposta/', 
            {'answer': alternative2.id}
        )
        
        self.assertEqual(
            False,
            response_answer.context["is_correct"]
        )