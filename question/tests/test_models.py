import pytest

from question.models import Questao


@pytest.fixture
def create_questao(db):
    questao = Questao.objects.create(
        numero = 99,
        enunciado = 'Qual a soma de 2 + 7?',
        alternativa_a = '1',
        alternativa_b = '3',
        alternativa_c = '5',
        alternativa_d = '8',
        alternativa_e = '9',
        alternativa_correta = 'e',
        ativa = True,
    )
    return questao


@pytest.mark.django_db
def test_str_questao(create_questao):
    questao = create_questao
    assert str(questao) == '99 - Qual a soma de 2 + 7?'


@pytest.mark.django_db
def test_fields_questao(create_questao):
    questao = create_questao
    assert questao.numero == 99
    assert questao.enunciado == 'Qual a soma de 2 + 7?'
    assert questao.alternativa_a == '1'
    assert questao.alternativa_b == '3'
    assert questao.alternativa_c == '5'
    assert questao.alternativa_d == '8'
    assert questao.alternativa_e == '9'
    assert questao.alternativa_correta == 'e'
    assert questao.ativa != False


@pytest.mark.django_db
def test_questao_create_object():
    questao = Questao.objects.create(
        numero = 1,
        enunciado = 'Qual a soma de 2 + 7?',
        alternativa_a = '0',
        alternativa_b = '1',
        alternativa_c = '2',
        alternativa_d = '9',
        alternativa_e = '11',
        alternativa_correta = 'd',
        ativa = True,
    )
    assert Questao.objects.count() == 1

