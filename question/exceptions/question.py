
class QuestionNotFound(Exception):
    def __init__(self, app, module, scope, **kwargs):
        self.app = app
        self.module = module
        self.scope = scope
        self.action = kwargs.get('action')

    def __str__(self):
        return ('QuestionNotFound -> '
                f'{self.app}.'
                f'{self.module}.'
                f'{self.scope}.'
                f'{self.action}'
                ).replace('\n', '')
