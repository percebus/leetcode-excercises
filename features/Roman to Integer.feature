Feature: Roman to Integer

  # SRC: https://leetcode.com/problems/roman-to-integer/
  #
  # Roman numerals are usually written largest to smallest from left to right.
  #
  # Constraints:
  # * 1 <= s.length <= 15
  # * s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
  # * It is guaranteed that s is a valid roman numeral in the range [1, 3999].


  # Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
  # Symbol       Value
  # I             1
  # V             5
  # X             10
  # L             50
  # C             100
  # D             500
  # M             1000
  Scenario Outline: Symbols
    Given a roman <numeral>
     When I run roman_to_int
     Then convert it to an <integer>

  Examples:
    | numeral | integer |
    | I       |       1 |
    | V       |       5 |
    | X       |      10 |
    | L       |      50 |
    | C       |     100 |
    | D       |     500 |
    | M       |    1000 |


  # For example,
  #  * 2 is written as II in Roman numeral, just two one's added together.
  #  * 12 is written as XII, which is simply X + II.
  #  * The number 27 is written as XXVII, which is XX + V + II.
  Scenario Outline: Addition
    Given a roman <numeral>
     When I run roman_to_int
     Then convert it to an <integer>

  Examples:
    | numeral | integer |     explanation     |
    | II      |       2 | 1 + 1               |
    | III     |       3 | 1 + 1 + 1           |
    | V       |       5 | 5                   |
    | VI      |       6 | 5 + 1               |
    | VII     |       7 | 5 + 1 + 1           |
    | XII     |      12 | 10 + 2              |
    | XXVII   |      27 | 10 + 10 + 5 + 1 + 1 |
    | LVIII   |      58 | 50 + 5 + 1 + 1 + 1  |
    | MM      |    2000 | 1000 + 1000         |


  # 'I' can be placed before 'V' (5) and 'X' (10) to make 4 and 9.
  Scenario Outline: Prefix: 'I'
    Given a roman <numeral>
     When I run roman_to_int
     Then convert it to an <integer>

  Examples:
    | numeral | integer |                explanation                  |
    |  VI     |       6 | 5 + 1                                       |
    |  V      |       5 |                                             |
    | IV      |       4 | 'I' can be placed before 'V'  (5) to make 4 |
#   |         |         |                                             |
    |  XI     |      11 | 10 + 1                                      |
    |  X      |      10 | 10                                          |
    | IX      |       9 | 'I' can be placed before 'X' (10) to make 9 |


  # 'X' can be placed before 'L' (50) and 'C' (100) to make 40 and 90.
  Scenario Outline: Prefix: 'X'
    Given a roman <numeral>
     When I run roman_to_int
     Then convert it to an <integer>

  Examples:
    | numeral | integer |                explanation                    |
    |  LX     |      60 | 50 + 10                                       |
    |  L      |      50 | 50                                            |
    | XL      |      40 | 'X' can be placed before 'L'  (50) to make 40 |
#   |         |         |                                               |
    |  CX     |     110 | 100 + 10                                      |
    |  C      |     100 | 100                                           |
    | XC      |      90 | 'X' can be placed before 'C' (100) to make 90 |


  # 'C' can be placed before 'D' (500) and 'M' (1000) to make 400 and 900.
  Scenario Outline: Prefix: 'C'
    Given a roman <numeral>
     When I run roman_to_int
     Then convert it to an <integer>

  Examples:
    | numeral | integer |               explanation                       |
    |  DC     |     600 | 500 + 100                                       |
    |  D      |     500 |                                                 |
    | CD      |     400 | 'C' can be placed before 'D'  (500) to make 400 |
#   |         |         |                                                 |
    |  MC     |    1100 | 1000 + 100                                      |
    |  M      |    1000 | 1000                                            |
    | CM      |     900 | 'C' can be placed before 'M' (1000) to make 900 |


  Scenario Outline: Complex
    Given a roman <numeral>
     When I run roman_to_int
     Then convert it to an <integer>

  Examples:
    | numeral   | integer |
    | MCMXCIV   |    1994 |
    | MCMLXXXII |    1982 |
    | MCMLXXXIV |    1984 |


  # FIXME throw
  Scenario Outline: Invalid
    Given a roman <numeral>
     When I run roman_to_int
#    Then throw an exception # TODO FIXME
     Then convert it to an <integer>

  Examples:
    | numeral | integer |
    | IIII    |       4 |
    | IIIII   |       5 |
    | VIIII   |       9 |
    | XXXX    |      40 |
    | XXXXX   |      50 |
    | XXXXXX  |      60 |
    | LXXXX   |      90 |
    | CCCC    |     400 |
    | DCCCC   |     900 |
    | DD      |    1000 |
