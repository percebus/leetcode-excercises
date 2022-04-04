Feature: Merge k Sorted Lists

  # SRC: https://leetcode.com/problems/merge-k-sorted-lists/
  #
  # Constraints:
  #  * k == lists.length
  #  * 0 <= k <= 10^4
  #  * 0 <= lists[i].length <= 500
  #  * -10^4 <= lists[i][j] <= 10^4
  #  * lists[i] is sorted in ascending order.
  #  * The sum of lists[i].length will not exceed 10^4


  Scenario Outline: Simple
    Given an <array> of k linked-lists lists
#     And each linked-list is sorted in ascending order
     When I call mergeKLists
     Then it returns all the linked-lists merged into one sorted linked-list as <result>

  Examples:
  |     array          |    result     |
  | [ {1} ]            | {1}           |
  | [ {1→2} ]          | {1→2}         |
  | [ {1→2→3} ]        | {1→2→3}       |
  | [ {1→2→3→4} ]      | {1→2→3→4}     |
  | [ {1→2→3→4→5} ]    | {1→2→3→4→5}   |
  | [ {1→2→3→4→5→6} ]  | {1→2→3→4→5→6} |


  Scenario Outline: Complex
    Given an <array> of k linked-lists lists
#     And each linked-list is sorted in ascending order
     When I call mergeKLists
     Then it returns all the linked-lists merged into one sorted linked-list as <result>

  Examples:
  |          array              |       result      |
  | [ {1→2}, {3→4}, {5→6} ]     | {1→2→3→4→5→6}     |
  | [ {1→4→5}, {1→3→4}, {2→6} ] | {1→1→2→3→4→4→5→6} |


  Scenario Outline: Empty
    Given an <array> of k linked-lists lists
#     And each linked-list is sorted in ascending order
     When I call mergeKLists
     Then it returns all the linked-lists merged into one sorted linked-list as <result>
  Examples:
  |  array  | result |
  |   []    |   {}   |
  | [ {} ]  |   {}   |
