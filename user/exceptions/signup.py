class SignupDataInvalid(Exception):
    def __init__(self, code):
        self.code = code
