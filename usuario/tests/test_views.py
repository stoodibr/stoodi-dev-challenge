import pytest
from django.urls import reverse

from django.contrib.auth.models import User
from question.tests.test_models import create_questao


@pytest.fixture
def create_user(db):
    user = User.objects.create_user(
            username = 'user_test',
            password = 'pass_test')
    return user


@pytest.mark.django_db
def test_status_code_login_url(client):
    url_str = reverse('login')
    response = client.get(url_str)
    assert response.status_code == 200


@pytest.mark.django_db
def test_status_code_cadastro_url(client):
    url_str = reverse('cadastro')
    response = client.get(url_str)
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_user_created(client, create_user, create_questao):
    url_str = reverse('login')
    url_base_str = reverse('question')

    data = client.post(url_str, data={
        'username':'user_test', 'password': 'pass_test'})

    data_login = client.get(url_base_str)
    user_context = data_login.context['user']

    assert user_context == User.objects.get(username='user_test')
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_cadastro_user(client, create_questao):
    url_str = reverse('cadastro')

    data = client.post(url_str, data={
        'username':'user_form',
        'password1': 'pass_test',
        'password2': 'pass_test'
        })

    confirma_user_cadastrado = User.objects.filter(username='user_form').exists()

    assert confirma_user_cadastrado == True
    assert User.objects.count() == 1
