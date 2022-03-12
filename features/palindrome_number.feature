Feature: Palindrome Number
# SRC: https://leetcode.com/problems/palindrome-number/
#
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.
#
# Constraints
#  * -2^31 <= x <= 2^31 - 1


  Scenario Outline: True
    Given an integer number <x>
     When I run is_palindrome
     Then return True if x is palindrome integer
  Examples:
    |    x  | mirrored |                 explaination                                |
    |     1 | 1        |     1 == 1                                                  |
    |   121 | 121      | 121 reads as 121 from left to right and from right to left. |
    |  1221 | 1221     |  1221 == 1221                                               |
    | 12321 | 12321    | 12321 == 12321                                              |


  Scenario Outline: False
    Given an integer number <x>
     When I run is_palindrome
     Then return False if x is NOT palindrome integer
  Examples:
    |   x  | mirrored |                                        explaination                                                       |
    |   -1 | 1-       |  -1 != 1-                                                                                                 |
    |   12 | 21       |  12 != 21                                                                                                 |
    |  123 | 321      | 123 != 321                                                                                                |
    | -121 | 121-     | From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome. |
    |   10 | 01       | Reads 01 from right to left. Therefore it is not a palindrome.                                            |
