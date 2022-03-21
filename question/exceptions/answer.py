from question.constants import APP_NAME


class AnswerNotFound(Exception):
    def __init__(self, module, scope, **kwargs):
        self.app = APP_NAME
        self.module = module
        self.scope = scope
        self.action = kwargs.get('action')

    def __str__(self):
        return ('AnswerNotFound -> '
                f'{self.app}.'
                f'{self.module}.'
                f'{self.scope}.'
                f'{self.action}'
                ).replace('\n', '')
