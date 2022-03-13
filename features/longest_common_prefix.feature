Feature: Longest Common Prefix
# SRC: https://leetcode.com/problems/longest-common-prefix/
#
# Constraints:
#  * 1 <= strs.length <= 200
#  * 0 <= strs[i].length <= 200
#  * strs[i] consists of only lower-case English letters.

  Scenario Outline: common prefix
     Given an array of <words>
      When I call longest_common_prefix
      Then find the longest common <prefix> string amongst an array of strings
  Examples:
  |  words                       | prefix |
  | ['flower', 'flow', 'flight'] | 'fl'   |
  | ['']                         | ''     |


  Scenario Outline: no common prefix
     Given an array of <words>
      When I call longest_common_prefix
      Then return an empty <prefix>
  Examples:
  |  words                       | prefix |
  | ['dog', 'racecar', 'car']    | ''     |
  | ['']                         | ''     |
