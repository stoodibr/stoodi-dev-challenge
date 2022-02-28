from user.forms import UserForm
from django.test import TestCase
from django.contrib.auth.models import User

class BaseModel(TestCase):

    def setUp(self):
        self.user_form = UserForm()
        self.user = User.objects.create(username='user_test',
                                        first_name='Tester', 
                                        last_name='Silva', 
                                        email='test@test.com', 
                                        password='test123'
                                        )