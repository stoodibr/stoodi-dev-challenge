from .base_model import BaseModel
from django.urls import reverse


class QuestionViewsTestCase(BaseModel):

    def test_question_view_first_page(self):

        response = self.client.get(reverse('question',  kwargs={}))
        
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.charset, 'utf-8')
        self.assertEquals(response.get('content-type'), 'text/html; charset=utf-8')

    def test_question_view_with_param(self):

        response = self.client.post(reverse('question_by_id', kwargs={'id': '1'}))
        
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.charset, 'utf-8')
        self.assertEquals(response.get('content-type'), 'text/html; charset=utf-8')


    def test_log_by_user_authenticated(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('user_log', kwargs={}))
        
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.charset, 'utf-8')
        self.assertEquals(response.get('content-type'), 'text/html; charset=utf-8')

    def test_log_by_user_redirect_unauthenticated_user(self):
      
        response = self.client.get(reverse('user_log', kwargs={}))
        
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.charset, 'utf-8')
        self.assertEquals(response.get('content-type'), 'text/html; charset=utf-8')

