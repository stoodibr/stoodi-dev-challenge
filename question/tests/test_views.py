import pytest
from django.urls import reverse

from question.models import Questao


@pytest.fixture
def create_questao(db):
    questao = Questao.objects.create(
        numero = 3,
        enunciado = 'Qual a soma de 2 + 5?',
        alternativa_a = '9',
        alternativa_b = '22',
        alternativa_c = '7',
        alternativa_d = '1',
        alternativa_e = '1212',
        alternativa_correta = 'c',
        ativa = True,
    )
    return questao


@pytest.mark.django_db
def test_ordered_answers(client, create_questao):
    url_str = reverse('question')

    data = client.get(url_str)
    answers = data.context['answers']

    ordered_answers = dict(sorted(answers.items()))

    assert  list(ordered_answers.keys()) == list(answers.keys())


@pytest.mark.django_db
def test_check_question_data(client, create_questao):
    questao = create_questao
    url_str = reverse('question')

    data = client.get(url_str)
    question_text = data.context['question_text']
    question_num = data.context['question_num']

    assert questao.enunciado == question_text
    assert questao.numero == question_num




