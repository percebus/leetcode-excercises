Feature: Palindrome Number

  Scenario Outline: True
    Given an integer number <x>
    When I run is_palindrome(x)
    Then return True if x is palindrome integer
  Examples:
    |    x  | mirrored | Explaination                                                |
    |   121 | 121      | 121 reads as 121 from left to right and from right to left. |
    |  1221 | 1221     |  1221 VS 1221.                                              |
    | 12321 | 12321    | 12321 VS 12321.                                             |


  Scenario Outline: False
    Given an integer number <x>
    When I run is_palindrome(x)
    Then return False if x is NOT palindrome integer
  Examples:
    |   x  | mirrored | Explaination                                                                                              |
    | -121 | 121-     | From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome. |
    |   10 | 01       | Reads 01 from right to left. Therefore it is not a palindrome.                                            |
