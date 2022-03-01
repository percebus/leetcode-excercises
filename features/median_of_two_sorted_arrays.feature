Feature: Median of 2 sorted arrays
  Scenario Outline: odd-sized array
    Given two sorted arrays <array1> and <array2>
#     And of size <m> and <n> respectively # TODO
     When I call find_median
     Then return the <median> of the two sorted arrays
#     And the overall run time complexity should be O(log (m+n)) # TODO
  Examples:
  |     array1      | array2 | median |
  |     [1, 3]      |   [2]  |      2 |
  | [1, 2, 3, 4, 5] |   []   |      3 |


  Scenario Outline: median of 2 numbers in a even-sized list
    Given two sorted arrays <array1> and <array2>
#     And of size <m> and <n> respectively TODO
     When I call find_median
     Then return the <median> of the two sorted arrays
#     And the overall run time complexity should be O(log (m+n)) # TODO
  Examples:
  | array1 | array2 | median |
  | [1, 2] | [3, 4] |    2.5 |
