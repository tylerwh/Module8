import unittest
from more_fun_with_collections import set_membership


class TestSetMembership(unittest.TestCase):
  def test_in_set_true(self):
    test_set = ('abcdef')
    element = 'd'
    self.assertTrue(set_membership.in_set(test_set, element))


  def test_in_set_false(self):
    false_test_set = ('12345')
    false_element = '0'
    self.assertFalse(set_membership.in_set(false_test_set, false_element))


if __name__ == "__main__":
  unittest.main()