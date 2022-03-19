from django.test import TestCase

from question.utils.core import sort_dict_by_keys


class TestQuestionsUtilsCore(TestCase):
    def test_dict_is_sorted_correctly(self):
        """SHOULD return dict sorted by keys"""

        self.payload = {
            'e': 4,
            'b': 1,
            'd': 3,
            'a': 0,
            'c': 2,
        }

        dict_expected = {
            'a': 0,
            'b': 1,
            'c': 2,
            'd': 3,
            'e': 4,
        }

        dict_result = sort_dict_by_keys(self.payload)

        self.assertDictEqual(dict_expected, dict_result)
