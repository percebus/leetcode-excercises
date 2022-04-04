Feature: Reverse to Make Equal

  # SRC: https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=2869293499822992&c=274804128169977&ppid=454615229006519&practice_plan=0
  #
  # Constraints:
  #  * All integers in array are in the range [0, 1,000,000,000].

  Scenario Outline: True
    Given two arrays <A> and <B>
#     And both <A> and <B> are of length <N>
     When I run are_they_similar
     Then are_they_similar returns True
  Examples:
    | N |  A      |    B     |   exlanation   |
    | 1 | 1       | 1        |                |
    | 2 | 1,2     | 1,2      |                |
    | 3 | 1,2,3   | 1,2,3    |                |
    | 4 | 1,2,3,4 | 1,2,3,4  |                |
    | 4 | 1,2,3,4 | 1,4,3,2  | [4,3] >> [3,4] |
    | 4 | 1,2,3,4 | 1,2,4,3  | [4,3] >> [3,4] |
    | 4 | 1,2,3,4 | 4,3,2,1  | palindrome     |


  Scenario Outline: False
    Given two arrays <A> and <B>
#     And both <A> and <B> are of length <N>
     When I run are_they_similar
     Then are_they_similar returns False
  Examples:
    | N |    A    |    B    |
    | 4 | 1,2,3,4 | 1,2,3,5 |
