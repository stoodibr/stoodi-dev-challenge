from question.models import CustomLogQuestions

class CustomLogs():
    """ This class must be responsible to manipulate Questions Logs Model """

    def __save_new_log(self, answer, is_correct, user):    
        log = CustomLogQuestions(selected_answer=answer, is_correct=is_correct, user=user)
        log.save()

    def add_log(self, answer, is_correct, user):
        try:
            self.__save_new_log(answer, is_correct, user)
        except Exception as e:
            raise Exception(f'Erro ao inserir novo log de resultados. {str(e)}')

    def get_logs_by_user(self, user):
        try:
            return {"logs" : CustomLogQuestions.objects.filter(user=user)}
        except Exception as e:
            raise Exception(f'Erro ao recuperar log de usuário. {str(e)}')