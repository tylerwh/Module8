"""
Author: Tyler Hochstetler
The purpose of this program is to practice passing arguments to functions.
"""


def average_scores(a_dict):
  """Accepts a dictionary as the only parameter and returns the average scores.
  :param a_dict: Dictionary argument containing the test scores to be calculated
  :return: Average test scores
  """
  scores = 0
  for d in a_dict:
    # print(a_dict[d])
    scores += float(a_dict[d])
  
  # print("Length of a_dict")
  # print(len(a_dict))
  # print("Average to be returned")
  # print(scores/len(a_dict))
  return scores/len(a_dict)



def score_input(test_name, test_score=0, invalid_message="Invalid test score, try again!"):
  """ This function takes the above parameters, validates them, then returns a concatenated test_name and test_score
  :param test_name: required, name to be used
  :param test_score: default is 0, but can take a number as an argument 
  :param invalid_message: this displays if user inputs the incorrect number
  :returns: the test_name and test_score concatenated together
  """
  try:
    if test_score < 0 or test_score > 100:
      return invalid_message
    else:
      return {test_name: test_score}
      # return test_name + ": " + str(test_score)
  except:
    return ValueError


if __name__ == "__main__":
  
  num_scores = int(input("How many scores would you like to input? "))
  scores_dict = dict()
  
  i = 0
  while i < num_scores:
    score = input("Input score {:}: ".format(i+1))
    scores_dict.update({i+1:score})
    i += 1

  avg_score = average_scores(scores_dict)
  first_name = "Johnny"

  try:
    johnny = score_input(first_name, avg_score)
    print(johnny)
  except ValueError:
    print(ValueError)
