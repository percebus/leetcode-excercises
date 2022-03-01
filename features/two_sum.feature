Feature: Two Sum
# SRC: https://leetcode.com/problems/two-sum/
#
# Constraints:
#   * 2 <= nums.length <= 104
#   * -109 <= nums[i] <= 109
#   * -109 <= target <= 109
#   * Only one valid answer exists.

  Scenario Outline: only
     Given an <array> of integers nums
       And an integer <target>
      When I call two_sum
      Then return <indices> of the <two_numbers>
       And they add up to <target>
  Examples:
  |     array      | target | indices | two_numbers |
  | [2, 7, 11, 15] |      9 |  [0, 1] |    [2, 7]   |
  | [3, 2, 4]      |      6 |  [1, 2] |    [2, 4]   |
  | [3, 3]         |      6 |  [0, 1] |    [3, 3]   |
