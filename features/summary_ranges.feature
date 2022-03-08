Feature: Summary Ranges
# SRC: https://leetcode.com/problems/summary-ranges/
#
# Constraints:
#   * 0 <= nums.length <= 20
#   * -231 <= nums[i] <= 231 - 1
#   * All the values of nums are unique.
#   * nums is sorted in ascending order.

  Scenario Outline: ->
    Given a sorted unique integer <array>
    When I call summary_ranges
    Then return the <expected> smallest sorted list of ranges that cover all the numbers in the array exactly
  Examples:
  |         array         |        expected            |
  | [0, 1, 2, 4, 5, 7]    | ['0->2', '4->5', '7']      |
  | [0, 2, 3, 4, 6, 8, 9] | ['0', '2->4', '6', '8->9'] |
