from typing import Dict

from django.forms import ValidationError
from django.http.request import HttpRequest
from django.core.validators import validate_email

from user.models import CustomUser
from user.exceptions.signup import SignupDataInvalid


def signup_validator(
        user_email: str,
        user_password: str,
        user_name: str) -> Dict[str, str]:

    if not(user_email):
        raise SignupDataInvalid('REQUIRED_EMAIL')

    if not(user_password):
        raise SignupDataInvalid('REQUIRED_PASSWORD')

    if not(user_name):
        raise SignupDataInvalid('REQUIRED_NAME')

    try:
        validate_email(user_email)
    except ValidationError:
        raise SignupDataInvalid('INVALID_EMAIL')

    is_registered_email = (
        CustomUser.objects
        .filter(email=user_email)
        .exists()
    )

    if is_registered_email is True:
        raise SignupDataInvalid('EMAIL_ALREADY_REGISTERED')

    user_name_split = user_name.title().split(' ')
    user_first_name = user_name_split[0]
    user_last_name = (
        user_name_split[-1]
        if len(user_name_split) > 1
        else ''
    )

    return {
        'first_name': user_first_name,
        'last_name': user_last_name,
        'email': user_email,
        'password': user_password
    }
