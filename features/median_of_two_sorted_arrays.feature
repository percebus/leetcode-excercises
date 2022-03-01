Feature: Median of 2 sorted arrays
  Scenario Outline: odd-sized array
    Given arrays <array1> and <array2>
    When I call find_median
    Then I get the <expected> result

  Examples:
  |     array1      | array2 | expected |
  |     [1, 3]      |   [2]  |      2   |
  | [1, 2, 3, 4, 5] |   []   |      3   |


  Scenario Outline: median of 2 numbers in a even-sized list
    Given arrays <array1> and <array2>
    When I call find_median
    Then I get the <expected> result
  Examples:
  | array1 | array2 | expected |
  | [1, 2] | [3, 4] |      2.5 |
