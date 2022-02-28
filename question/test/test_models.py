from .base_model import BaseModel

class QuestionModelsTestCases(BaseModel):

    def test_model_question_creation(self):

        self.assertEquals(self.question.text, 'just a test question')
    
    def test_model_answer_creation(self):

        self.assertEquals(self.answer_true.text, 'just a test answer')
        self.assertEquals(self.answer_false.text, 'just another test answer')
        self.assertEquals(self.answer_true.question_id, self.question)
        self.assertEquals(self.answer_false.question_id, self.question)

    def test_model_customlogquestions_creaton(self):

        self.assertEquals(self.log.user, self.user)    
        self.assertEquals(self.log.selected_answer, self.answer_false)    
        self.assertEquals(self.log.is_correct, str(self.answer_false.is_correct))    
        self.assertEquals(str(self.log), f'{self.log.date} - Tester  --  just another test answer  -- Resposta Errada')    
        self.assertEquals(str(self.log_true), f'{self.log_true.date} - Tester  --  just a test answer  -- Resposta Correta')
    



