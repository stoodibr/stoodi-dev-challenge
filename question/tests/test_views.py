import pytest
from django.urls import reverse

from question.models import Questao, Resposta
from usuario.tests.test_views import create_user

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


@pytest.mark.django_db
def test_answers_by_database(client, create_questao):
    questao = create_questao
    url_str = reverse('question_answer')

    data = client.post(url_str, data={'identificador':questao.identificador, 'answer': 'c'})

    questao_db = data.context['questao']
    answer = data.context['answer']

    assert  questao_db.pk == questao.pk
    assert  answer == questao.alternativa_correta


@pytest.mark.django_db
def test_answers_whith_next_question(client):
    questao1 = Questao.objects.create(
        numero = 1, enunciado = 'Qual a soma de 2 + 2?',
        alternativa_a = '9', alternativa_b = '22', alternativa_c = '7', alternativa_d = '4',
        alternativa_e = '1212', alternativa_correta = 'd', ativa = True,
    )
    questao2 = Questao.objects.create(
        numero = 2, enunciado = 'Qual a soma de 2 + 2?',
        alternativa_a = '9', alternativa_b = '22', alternativa_c = '7', alternativa_d = '4',
        alternativa_e = '1212', alternativa_correta = 'd', ativa = True,
    )
    url_str = reverse('question_answer')

    dados1 = client.post(url_str, data={'identificador':questao1.identificador, 'answer': 'd'})
    proxima_questao1 = dados1.context['proxima_questao']

    dados2 = client.post(url_str, data={'identificador':questao2.identificador, 'answer': 'd'})
    proxima_questao2 = dados2.context['proxima_questao']

    assert Questao.objects.count() == 2
    assert proxima_questao1 == questao2
    assert proxima_questao2 == questao1


@pytest.mark.django_db
def test_resposta_generate_by_answer_not_authenticated(client, create_questao):
    questao = create_questao
    url_str = reverse('question_answer')

    data = client.post(url_str, data={'identificador':questao.identificador, 'answer': 'c'})

    assert Resposta.objects.count() == 0


@pytest.mark.django_db
def test_resposta_generate_by_answer_authenticated(client, create_questao, create_user):
    questao = create_questao
    url_str = reverse('question_answer')
    url_login_str = reverse('login')

    data = client.post(url_login_str, data={
        'username':'user_test', 'password': 'pass_test'})

    data = client.post(url_str, data={'identificador':questao.identificador, 'answer': 'c'})

    assert Resposta.objects.count() == 1


@pytest.mark.django_db
def test_status_code_log_questoes_url_not_autenticated(client):
    url_str = reverse('log_questoes')
    response = client.get(url_str)
    assert response.status_code != 200


@pytest.mark.django_db
def test_status_code_log_questoes_url_autenticated(client, create_user, create_questao):
    questao = create_questao

    url_login_str = reverse('login')
    data = client.post(url_login_str, data={
        'username':'user_test', 'password': 'pass_test'})

    url_str_resposta = reverse('question_answer')
    data = client.post(url_str_resposta, data={'identificador':questao.identificador, 'answer': 'c'})

    url_str = reverse('log_questoes')
    response = client.get(url_str)
    respostas_lista = response.context['respostas']

    assert len(respostas_lista) == 1
    assert response.status_code == 200