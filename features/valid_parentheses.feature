Feature: Valid Parentheses
# SRC: https://leetcode.com/problems/valid-parentheses/
#
# An input string is valid if:
#  * Open brackets must be closed by the same type of brackets.
#  * Open brackets must be closed in the correct order.
#
# Constraints:
#  * 1 <= s.length <= 104                    # TODO test
#  * s consists of parentheses only '()[]{}' # XXX? What if I don't like this


  Scenario Outline: invalid
    Given a <string> containing the characters '(', ')', '{', '}', '[' and ']'
     When I run is_valid
     Then determine that the input string is NOT valid
  Examples:
  | string |
  |   [    |
  |   ]    |
  |   (    |
  |   )    |
  |   {    |
  |   }    |
  |   (]   |
  |   (}   |
  |   [)   |
  |   [}   |
  |   {)   |
  |   {]   |

  Scenario Outline: valid
    Given a <string> containing the characters '(', ')', '{', '}', '[' and ']'
     When I run is_valid
     Then determine that the input string is valid
  Examples:
  | string |
  |   ()   |
  |   []   |
  |   {}   |
  | ()[]{} |
  | ({[]}) |
  | ([{}]) |
  | [{()}] |
  | [({})] |
  | {([])} |
  | {[()]} |

  Scenario Outline: valid w/ more characters
    Given a <string> containing the characters '(', ')', '{', '}', '[' and ']'
     When I run is_valid
     Then determine that the input string is valid
  Examples:
  |            string           |
  |  1+1                        |
  | (1+1)                       |
  |  1 +1                       |
  | (1 +1)                      |
  |  1 + 1                      |
  | (1 + 1)                     |
  | ((6+9) + (6x9))             |
  | [(1,2), (3,4), (5,6)]       |
  | {a:1, b:2, c:3}             |
  | {  a:  [ (1,2), (3,4) ]  }  |


  Scenario Outline: invalid w/ more characters
    Given a <string> containing the characters '(', ')', '{', '}', '[' and ']'
     When I run is_valid
     Then determine that the input string is NOT valid
  Examples:
  |            string          |
  | (1+1                       |
  |  1+1)                      |
  | (1 +1                      |
  |  1 +1)                     |
  | (1 + 1                     |
  |  1 + 1)                    |
  |  (6+9) + (6x9))            |
  | ((6+9) + (6x9)             |
  | ( 6+9) + (6x9))            |
  | ((6+9  + (6x9))            |
  | ((6+9) +  6x9))            |
  | ((6+9) + (6x9 )            |
  | [(1,2), (3,4), (5,6)       |
  |  (1,2), (3,4), (5,6)]      |
  | [(1,2 , (3,4), (5,6)]      |
  | [ 1,2), (3,4), (5,6)]      |
  | {a:1, b:2, c:3             |
  |  a:1, b:2, c:3}            |
  | {  a:  [ (1,2), (3,4) ]    |
  |    a:  [ (1,2), (3,4) ]  } |
  | {  a:  [ (1,2), (3,4)    } |
  | {  a:    (1,2), (3,4) ]  } |
  | {  a:  [ (1,2 , (3,4) ]  } |
  | {  a:  [  1,2), (3,4) ]  } |
  | {  a:  [ (1,2 , (3,4) ]  } |
  | {  a:  [ (1,2), (3,4  ]  } |
  | {  a:  [ (1,2),  3,4) ]  } |
