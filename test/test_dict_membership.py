import unittest
from more_fun_with_collections import dict_membership


class DictionaryTestCase(unittest.TestCase):
  def test_in_dict_true(self):
    dict_to_pass = {'Name': 'Johnny', 'Age': 3, 'School': 'Elm Elementary'}
    element = 'Age'
    self.assertTrue(dict_membership.in_dict(dict_to_pass, element))


  def test_in_dict_false(self):
    test_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7}
    key_element = 'C#'
    self.assertFalse(dict_membership.in_dict(test_dict, key_element))


if __name__ == "__main__":
    unittest.main()