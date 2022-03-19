from django.test import TestCase

from question.models import Question, Answer
from selecao.utils.database import queryset_to_dict


class TestSelecaoUtilsDatabase(TestCase):
    def setup(self):
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

    def test_queryset_to_dict(self):
        """SHOULD return dict from queryset"""

        answers = Answer.objects.all().values()

        dict_expected = {
            answer['letter']: answer['text']
            for answer in answers
        }

        dict_result = queryset_to_dict(answers, 'letter', 'text')

        self.assertFalse(dict_expected, dict_result)
