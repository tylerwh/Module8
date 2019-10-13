"""
Author: Tyler Hochstetler
The purpose of this program is to practice using dictionaries in Python.
"""


def in_dict(dictionary, element):
  """This method accepts a set and an element. Returns a boolean value stating if the element is in the set.
  :param dictionary: the dictionary set received as argument.
  :param element: the element received as argument to verify if in dictionary argument.
  :return: boolean true/false depending on if element in dictionary
  """
  if element in dictionary:
    return True
  else:
    return False


if __name__ == "__main__":
  pass
