
from django.test import TestCase


from question.models import Question, Answer
from question.utils.answer import check_answer
from question.exceptions.answer import AnswerNotFound


class TestQuestionsAnswerUtils(TestCase):
    def setUp(self):
        question = Question.objects.create(text='Foo')

        payload = [
            Answer(
                question=question,
                letter='a',
                text='Foo',
                is_correct=True
            ),
            Answer(
                question=question,
                letter='b',
                text='Foo',
                is_correct=False
            ),
            Answer(
                question=question,
                letter='c',
                text='Foo',
                is_correct=False
            ),
        ]

        Answer.objects.bulk_create(payload)

    def test_check_answer_correct(self):
        """SHOULD return True WHEN user answer is correct"""
        question_id = 1
        user_answer_letter = 'a'

        result = check_answer(question_id, user_answer_letter)

        self.assertTrue(result)

    def test_check_answer_incorrect(self):
        """SHOULD return False WHEN user answer is correct"""
        question_id = 1
        user_answer_letter = 'b'

        result = check_answer(question_id, user_answer_letter)

        self.assertFalse(result)

    def test_throws_no_question_found(self):
        """SHOULD throw NoQuestionFound WHEN question doens't exists"""
        question_id = 2

        user_answer_letter = 'a'

        self.assertRaises(
            AnswerNotFound,
            check_answer,
            question_id, user_answer_letter
        )
