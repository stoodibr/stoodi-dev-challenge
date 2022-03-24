import random
from django.test import TestCase
from question.models import QuestionSubmission

from question.tests.factories import (
    QuestionFactory,
    FACTORY_ORDERED_OPTIONS,
    CORRECT_OPTION,
    WRONG_OPTIONS,
)

INVALID_OPTION= 'Z'

class TestQuestionModel(TestCase):
    def test_get_ordered_options(self):
        question = QuestionFactory()
        self.assertEqual(question.get_ordered_options(), FACTORY_ORDERED_OPTIONS)

    def test_get_wrong_answer(self):
        question = QuestionFactory()
        random_wrong_option = random.choice(WRONG_OPTIONS)
        self.assertFalse(question.is_option_correct(random_wrong_option))

    def test_get_right_answer(self):
        question = QuestionFactory()
        self.assertTrue(question.is_option_correct(CORRECT_OPTION))

    def test_get_invalid_answer(self):
        question = QuestionFactory()
        with self.assertRaises(KeyError):
            question.is_option_correct(INVALID_OPTION)

    def test_get_next_question_with_only_one_question_on_db(self):
        question = QuestionFactory()
        self.assertIsNone(question.get_next_question_id())

    def test_get_next_question_with_two_questions_on_db(self):
        first_question = QuestionFactory()
        next_question = QuestionFactory(text="this is another question")
        self.assertEqual(first_question.get_next_question_id(), next_question.id)

        self.assertEqual(next_question.get_next_question_id(), first_question.id)

    def test_get_next_question_with_two_questions_not_in_sequence_on_db(self):
        """
        Deleting a question shouldnt make the behaviour change
        """
        first_question = QuestionFactory()
        next_question = QuestionFactory(text="this is another question")
        third_question = QuestionFactory(text="this is the third question")
        next_question.delete()
        self.assertEqual(first_question.get_next_question_id(), third_question.id)

        self.assertEqual(third_question.get_next_question_id(), first_question.id)


class TestQuestionView(TestCase):
    def test_get_question(self):
        question = QuestionFactory()
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "question/question.html")
        self.assertEqual(response.context["question"], question)

    def test_get_question_no_questions_in_db(self):
        response = self.client.get("/")
        self.assertContains(
            response,
            "There are no questions on our database. Please contact an administrator.",
            status_code=404,
        )

    def test_get_question_invalid_id(self):
        QuestionFactory()
        response = self.client.get("/122233/")
        self.assertContains(
            response,
            "Question does not exist.",
            status_code=404,
        )
    
    def test_post_question_correct_answer(self):
        question = QuestionFactory()
        response = self.client.post("/", {"question_id": question.id, "answer": CORRECT_OPTION})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "question/answer.html")
        self.assertEqual(response.context["is_correct"], True)
        self.assertEqual(response.context["next_question_id"], None)
        self.assertEqual(response.context["current_question_id"], str(question.id))
        self.assertTrue(QuestionSubmission.objects.all().first().is_correct_answer())

    def test_post_question_wrong_answer(self):
        question = QuestionFactory()
        response = self.client.post("/", {"question_id": question.id, "answer": random.choice(WRONG_OPTIONS)})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "question/answer.html")
        self.assertEqual(response.context["is_correct"], False)
        self.assertEqual(response.context["next_question_id"], None)
        self.assertEqual(response.context["current_question_id"], str(question.id))
        self.assertFalse(QuestionSubmission.objects.all().first().is_correct_answer())

    def test_post_question_invalid_answer(self):
        question = QuestionFactory()
        response = self.client.post("/", {"question_id": question.id, "answer": INVALID_OPTION})
        self.assertContains(
            response,
            "The answer provided is not a valid option.",
            status_code=400,
        )
    
    def test_post_invalid_question_id(self):
        question = QuestionFactory()
        response = self.client.post("/233/", {"question_id": question.id, "answer": INVALID_OPTION})
        self.assertContains(
            response,
            "Question does not exist.",
            status_code=404,
        )