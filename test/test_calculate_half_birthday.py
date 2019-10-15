import unittest
import datetime
from more_fun_with_collections import calculate_half_birthday as chf


class TestHalfBirthday(unittest.TestCase):
  def test_half_birthday(self):
    b_day = datetime.date(2019, 2, 14)
    result = datetime.date(2020, 8, 14)
    self.assertAlmostEqual(chf.half_birthday(b_day), result)


if __name__ == "__main__":
    unittest.main()