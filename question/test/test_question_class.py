from .base_model import BaseModel

class QuestionResquestTestCases(BaseModel):

    def test_questionrequest_class_method_get_context(self):

        test_context = self.question_request_class.get_context()
        correct_context = {
            'question': self.question,
            'answers': {'a': self.answer_true , 'b': self.answer_false}
        }
        self.assertEqual(test_context, correct_context)

    def test_questionrequest_class_method_get_question_result(self):

        expected_response = self.question_request_class.get_question_result(self.answer_true.id)

        self.assertEqual(expected_response[0], self.answer_true.is_correct)
        self.assertEqual(expected_response[1], self.answer_true.text)
        
    def test_questionrequest_class_method_get_current_question(self):
        
        expected_response = self.question_request_class.get_current_question()
        self.assertEqual(expected_response, self.question.id)

    def test_questionrequest_class_method_get_next_question_id(self):
        
        expected_response = self.question_request_class.get_next_question_id()
        self.assertEqual(expected_response, self.question.id)
  



    