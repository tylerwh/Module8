"""
Author: Tyler Hochstetler
The purpose of this program is to implement a make-shift switch/case statement using functions and dictionaries.
"""


def switch_average(key):
  normalized_key = key.upper()
  averages = {
    "A": 90,
    "B": 80,
    "C": 70, 
    "D": 60,
    "F": 50
  }
  return averages.get(normalized_key)


if __name__ == "__main__":
    pass