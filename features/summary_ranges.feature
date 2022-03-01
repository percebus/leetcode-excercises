Feature: Summary Ranges
  Scenario Outline: ->
    Given a sorted unique integer <array>
    When I call summary_ranges
    Then return the <expected> smallest sorted list of ranges that cover all the numbers in the array exactly

  Examples:
  |         array         |        expected            |
  | [0, 1, 2, 4, 5, 7]    | ['0->2', '4->5', '7']      |
  | [0, 2, 3, 4, 6, 8, 9] | ['0', '2->4', '6', '8->9'] |
