import unittest
import datetime
from datetime import timedelta
from more_fun_with_collections import calculate_half_birthday as chf


class TestHalfBirthday(unittest.TestCase):
  def test_half_birthday(self):
    b_day = datetime.date(2019, 2, 14)
    result = b_day + timedelta(days=183.5)
    self.assertEqual(chf.half_birthday(b_day), result)


if __name__ == "__main__":
    unittest.main()