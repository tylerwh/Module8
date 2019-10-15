"""
Author: Tyler Hochstetler
The purpose of this program is to calculate the half birthday based upon the most recent birthday. 
"""
import datetime
from datetime import timedelta


def half_birthday(date):
  """Accepts a datetime of recent birthday and returns the date 6 months later."""
  half_b_day = date + timedelta(days=183.5)
  return half_b_day


if __name__ == "__main__":
    b_day = datetime.date(2019, 2, 14)
    print(b_day)