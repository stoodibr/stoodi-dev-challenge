from django.test import TestCase

from question.models import Answer, Question


class TestModels(TestCase):
    def test_get_question_without_id(self):
        # setup
        first_question = Question.objects.create(
            id=1, description='Qual a capital do Brasil?', correct_alternative='a'
        )

        # test
        question = Question.get_question()

        # assert
        self.assertEquals(question, first_question)

    def test_get_question_with_id(self):
        # setup
        second_question = Question.objects.create(
            id=2,
            description='Quem foi Américo Vespúcio?',
            correct_alternative='c'
        )
        # test
        question = Question.get_question(second_question.__dict__['id'])

        # assert
        self.assertEquals(question, second_question)

    def test_get_next_question_id(self):
        # setup
        current_question = Question.objects.create(
            id=3, description='Qual a capital do Brasil?', correct_alternative='a'
        )

        next_question = Question.objects.create(
            id=4, description='Qual a capital do Brasil?', correct_alternative='a'
        )

        # test
        next_question_id = Question.get_next_question_id(
            current_question.__dict__['id'])

        # assert
        self.assertEquals(next_question_id, next_question.__dict__['id'])

    def test_list_by_question(self):
        # setup
        third_question = Question.objects.create(
            id=5, description='Quem foi Maria Capitolina Santiago?', correct_alternative='b'
        )

        question_answers = []

        question_answers.append(Answer.objects.create(
            id=6, alternative='a', description='Personagem do livro O Alienista', question=third_question))
        question_answers.append(Answer.objects.create(
            id=7, alternative='b', description='Personagem do livro Dom Casmurro', question=third_question))

        question_answers_dict = {}
        for answer in question_answers:
            answer_dict = answer.__dict__
            question_answers_dict[answer_dict['alternative']
                                  ] = answer_dict['description']

        # test
        answers_list = Answer.list_by_question(third_question)

        # assert
        self.assertCountEqual(answers_list, question_answers_dict)
