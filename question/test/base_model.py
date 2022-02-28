from django.test import TestCase
from question.models import Question, Answer, CustomLogQuestions
from django.contrib.auth.models import User
from question.classes.questions_class import QuestionsRequest
from question.classes.custom_logs import CustomLogs


class BaseModel(TestCase):

    def setUp(self):

        self.user = User.objects.create(username='user_test', first_name='Tester', last_name='Silva', email='test@test.com', password='test123')
        self.question = Question.objects.create(text='just a test question')
        self.answer_true = Answer.objects.create(text='just a test answer', question_id=self.question, is_correct=True)
        self.answer_false = Answer.objects.create(text='just another test answer', question_id=self.question)
        
        self.log = CustomLogQuestions.objects.create(selected_answer=self.answer_false, is_correct=str(self.answer_false.is_correct), user=self.user)
        self.log_true = CustomLogQuestions.objects.create(selected_answer=self.answer_true, is_correct=str(self.answer_true.is_correct), user=self.user)

        self.question_request_class = QuestionsRequest(self.question.id)
        self.logger = CustomLogs()
        

