import unittest
from more_fun_with_collections import assign_average as a_avg

class TestSwitchCase(unittest.TestCase):
  def test_A_assign_average(self):
    a_letter = "A"
    a_expectation = 90
    self.assertEqual(a_avg.switch_average(a_letter), a_expectation)


  def test_B_assign_average(self):
    b_letter = "B"
    b_expectation = 80
    self.assertEqual(a_avg.switch_average(b_letter), b_expectation)


  def test_C_assign_average(self):
    c_letter = "C"
    c_expectation = 70
    self.assertEqual(a_avg.switch_average(c_letter), c_expectation)


  def test_D_assign_average(self):
    d_letter = "D"
    d_expectation = 60
    self.assertEqual(a_avg.switch_average(d_letter), d_expectation)


  def test_F_assign_average(self):
    f_letter = "F"
    f_expectation = 50
    self.assertEqual(a_avg.switch_average(f_letter), f_expectation)

  
  def test_non_key_assign_average(self):
    non_key = "E"
    expectation = KeyError
    with self.assertRaises(expectation):
      a_avg.switch_average(non_key)
    


if __name__ == "__main__":
    unittest.main()