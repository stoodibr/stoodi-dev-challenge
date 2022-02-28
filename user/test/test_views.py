from django.urls import reverse
from .base_model import BaseModel

class UserViewsTestCase(BaseModel):

    def test_signup_view_get(self):
        response = self.client.get(reverse('signup'))
        
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.charset, 'utf-8')
        self.assertEquals(response.get('content-type'), 'text/html; charset=utf-8')

    def test_signup_view_post(self):
        form_data =  {
                'username': '123123',
                'email': "user123@test.com",
                'first_name': "tester",
                'last_name': "silva",
                'password': "123123",
                'password2': "123123",
            }
        response = self.client.post(reverse('signup'), data=form_data)
        
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.charset, 'utf-8')
        self.assertEquals(response.get('content-type'), 'text/html; charset=utf-8')
    
    def test_signin_view_get(self):
        response = self.client.get(reverse('signin'))
        
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.charset, 'utf-8')
        self.assertEquals(response.get('content-type'), 'text/html; charset=utf-8')

    def test_logout_view_get_redirect(self):
        response = self.client.post(reverse('logout'))
        
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.charset, 'utf-8')
        self.assertEquals(response.get('content-type'), 'text/html; charset=utf-8')


    
