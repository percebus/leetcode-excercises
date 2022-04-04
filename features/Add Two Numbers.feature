Feature: Add Two Numbers

  # SRC: https://leetcode.com/problems/add-two-numbers/
  #
  # Constraints
  #  * The number of nodes in each linked list is in the range [1, 100].
  #  * 0 <= Node.val <= 9
  #  * It is guaranteed that the list represents a number that does not have leading zeros.


  Scenario Outline: _
    Given two non-empty linked lists <nodes1> and <nodes2> representing two non-negative integers
#     And each of their nodes contains a single digit
#     But the digits are stored in reverse order
     When I call addTwoNumbers
     Then I get the sum as a <result> linked list

  Examples:
  |    nodes1     |   nodes2  |     result      |   explanation   |
  | 2→4→3         | 5→6→4     | 7→0→8           | 342 + 465 = 807 |
  | 0             | 0         | 0               | 0               |
  | 9→9→9→9→9→9→9 | 9→9→9→9   | 8→9→9→9→0→0→0→1 | 9999999 + 9999  |
  | 0→1           | 5→0       | 5→1             | 10 + 05         |
  | 0             | 1         | 1               | 0 + 1           |
  | 1             | 0         | 1               | 1 + 0           |
  | 1→0→0→0→0     | 2→0→0→0→0 | 3               | 1 + 2           |
  | 0→0→0→0→1     | 0→0→0→0→2 | 0→0→0→0→3       | 10000 + 20000   |
