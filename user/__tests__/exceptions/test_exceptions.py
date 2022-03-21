from django.test import TestCase

from user.exceptions.signup import SignupDataInvalid


class TestUserExceptions(TestCase):
    def test_exception_code(self):
        err_code = 'TEST_CODE'

        try:
            raise SignupDataInvalid(err_code)
        except SignupDataInvalid as serr:
            self.assertEqual(serr.code, err_code)
