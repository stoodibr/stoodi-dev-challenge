import pytest
from django.contrib.auth.models import User

from question.models import Questao, Resposta


@pytest.fixture
def criar_usuario(db):
    user = User.objects.create_user(
            username = 'user_test',
            password = 'pass_test')
    return user

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


@pytest.fixture
def create_resposta_db(db, create_questao, criar_usuario):
    questao = create_questao
    user = criar_usuario
    resposta = Resposta.objects.create(
        usuario = user,
        questao = questao,
        alternativa_escolhida = 'e',
        alternativa_correta = True,
    )
    return resposta


@pytest.mark.django_db
def test_str_resposta(create_resposta_db):
    resposta = create_resposta_db
    assert str(resposta) == '{}'.format(resposta.data_resposta)

@pytest.mark.django_db
def test_save_resposta_db_count(create_resposta_db):
    resposta = create_resposta_db
    assert Resposta.objects.count() == 1

@pytest.mark.django_db
def test_fields_resposta(create_resposta_db, create_questao):
    questao = create_questao
    resposta = create_resposta_db
    assert resposta.questao == questao
    assert resposta.alternativa_escolhida == 'e'
    assert resposta.alternativa_correta == True