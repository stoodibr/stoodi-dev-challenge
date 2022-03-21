from django.test import TestCase
from user.exceptions.signup import SignupDataInvalid
from user.models import CustomUser

from user.utils.signup_validator import signup_validator


class TestUserSignupValidator(TestCase):
    def setUp(self):
        CustomUser.objects.create_user(
            email='foo@bar.com',
            first_name='Foo',
            last_name='Bar',
            password='pwd'
        )

    def test_code_when_throws_signup_data_invalid_exception(self):
        with self.assertRaises(SignupDataInvalid) as e:
            signup_validator(None, None, None)
            self.assertEqual(e.code, 'REQUIRED_EMAIL')

        with self.assertRaises(SignupDataInvalid) as e:
            signup_validator('foo@email.com', None, None)
            self.assertEqual(e.code, 'REQUIRED_PASSWORD')

        with self.assertRaises(SignupDataInvalid) as e:
            signup_validator('foo@email.com', 'bar', None)
            self.assertEqual(e.code, 'REQUIRED_NAME')

        with self.assertRaises(SignupDataInvalid) as e:
            signup_validator('foo', 'pwd', 'bar')
            self.assertEqual(e.code, 'INVALID_EMAIL')

        with self.assertRaises(SignupDataInvalid) as e:
            signup_validator('foo@bar.com', 'pwd', 'Foo Bar')
            self.assertEqual(e.code, 'EMAIL_ALREADY_REGISTERED')

    def test_return_payload_to_create_user(self):
        data_result = signup_validator(
            'foo@email.com', 'pwd', 'Foo Bar')

        data_expected = {
            'email': 'foo@email.com',
            'first_name': 'Foo',
            'last_name': 'Bar',
            'password': 'pwd'
        }

        self.assertDictEqual(data_result, data_expected)
