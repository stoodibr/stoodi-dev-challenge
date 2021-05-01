import pytest

from pytest_django.asserts import assertTemplateUsed
from django.core.exceptions import ObjectDoesNotExist

from question.models import Answer as AnswerModel, Question as QuestionModel


@pytest.fixture()
def question_answer():
    q1 = QuestionModel.objects.create(text='Quanto é 2 + 2?')
    a1 = AnswerModel.objects.create(question_ref=q1, choice_item='a', response='2')
    a2 = AnswerModel.objects.create(question_ref=q1, choice_item='b', response='3')
    a3 = AnswerModel.objects.create(question_ref=q1, choice_item='c', response='4')
    a4 = AnswerModel.objects.create(question_ref=q1, choice_item='d', response='5')
    a5 = AnswerModel.objects.create(question_ref=q1, choice_item='e', response='6')
    q1.correct_answer = a3
    q1.save()
    a1.save()
    a2.save()
    a3.save()
    a4.save()
    a5.save()

    q2 = QuestionModel.objects.create(text='Quanto é 5^2?')
    a6 = AnswerModel.objects.create(question_ref=q2, choice_item='a', response='25')
    a7 = AnswerModel.objects.create(question_ref=q2, choice_item='b', response='10')
    a8 = AnswerModel.objects.create(question_ref=q2, choice_item='c', response='5')
    a9 = AnswerModel.objects.create(question_ref=q2, choice_item='d', response='15')
    a10 = AnswerModel.objects.create(question_ref=q2, choice_item='e', response='0')
    q2.correct_answer = a6
    q2.save()
    a6.save()
    a7.save()
    a8.save()
    a9.save()
    a10.save()


def delete_db():
    QuestionModel.objects.all().delete()
    AnswerModel.objects.all().delete()


@pytest.mark.django_db
def test_question_no_correct_answer(client):
    q = QuestionModel.objects.create(text='Quanto é 2 + 2?')
    q.save()

    with pytest.raises(ObjectDoesNotExist):
        client.get('/')
        delete_db()


@pytest.mark.django_db
def test_sorted_answers(client):
    q = QuestionModel.objects.create(text='Quanto é 2 + 2?')
    a1 = AnswerModel.objects.create(question_ref=q, choice_item='b', response='2')
    a2 = AnswerModel.objects.create(question_ref=q, choice_item='a', response='4')
    q.correct_answer = a1
    q.save()
    a1.save()
    a2.save()

    response = client.get('/')
    sorted_answers = response.context.dicts[-1]['question'].object_list[0]['answers']
    assert ['a', 'b'] == [choice_item for choice_item in sorted_answers.keys()]

    assertTemplateUsed(response, 'question/question.html')

    delete_db()


@pytest.mark.django_db
def test_question(client, question_answer):
    response = client.get('/')

    assert response.status_code == 200
    assertTemplateUsed(response, 'question/question.html')

    delete_db()


@pytest.mark.django_db
def test_question_answer(client, question_answer):
    response = client.get('/resposta/')

    assert response.status_code == 200
    assertTemplateUsed(response, 'question/answer.html')

    delete_db()
