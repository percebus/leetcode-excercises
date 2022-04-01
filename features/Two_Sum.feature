Feature: Two Sum
# SRC: https://leetcode.com/problems/two-sum/
#
# Constraints:
#   * 2 <= nums.length <= 104
#   * -109 <= nums[i] <= 109
#   * -109 <= target <= 109
#   * Only one valid answer exists. # TODO TEST

  Scenario Outline: _
     Given an <array> of integers nums
       And an integer <target> number
      When I call two_sum
      Then return <indices> of the <two_numbers>
       And they add up to <target>
  Examples:
  |   case       |     array      | target | indices  | two_numbers |
  | 2, 7, 11, 15 | [2, 7, 11, 15] |      9 |  [0,  1] |   [2,  7]   |
  | 3, 2, 4      | [3, 2, 4]      |      6 |  [1,  2] |   [2,  4]   |
  | 3 x2         | [3, 3]         |      6 |  [0,  1] |   [3,  3]   |
#
  | 0-13         | range(0,  14)  |     13 |  [0, 13] |   [0, 13]   |
  | 1-13         | range(1,  14)  |     13 |  [0, 11] |   [1, 12]   |
  | 0-99         | range(0, 100)  |     13 |  [0, 13] |   [0, 13]   |
# | 0-200        | range(0, 201)  |     13 |  [0, 13] |   [0, 13]   | # Negative test: length.- outside constraints
# | 60 + 70      | [60, 70]       |    110 |  [0,  1] |  [60,  70]  | # Negative test: target.- outside constraints
# | 110 x2       | [110, 110]     |    240 |  [0,  1] | [110, 110]  | # Negative test: value.-  outside constraints
