# templates
SIGNUP_TEMPLATE = 'signup.html'
LOGIN_TEMPLATE = 'login.html'


# query strings redirect
QS_REDIRECT_SIGNUP_ERROR = {
    'GENERAL_ERROR': '?err=1',
    'REQUIRED_EMAIL': '?s=1',
    'REQUIRED_PASSWORD': '?s=2',
    'REQUIRED_NAME': '?s=3',
    'INVALID_EMAIL': '?s=4',
    'EMAIL_ALREADY_REGISTERED': '?s=5'
}

QS_REDIRECT_LOGIN_ERROR = {
    'INVALID_LOGIN': '?l=1'
}

QS_REDIRECT_LOGOUT = {
    'SUCCESS_LOGOUT': '?lt=1'
}
