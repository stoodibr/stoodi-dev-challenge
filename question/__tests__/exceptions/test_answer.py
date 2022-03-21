import imp
from django.test import TestCase

from question.constants import APP_NAME
from question.exceptions.answer import AnswerNotFound


class TestAnswerExceptions(TestCase):
    def test_answer_exception_representation(self):
        """ SHOULD return representation in pattern
            ExceptionName -> app.module.scope.action
        """
        repr_expected = f'AnswerNotFound -> {APP_NAME}.module.scope.action'
        repr_result = str(AnswerNotFound(
            module='module',
            scope='scope',
            action='action'
        ))

        self.assertEqual(repr_expected, repr_result)
