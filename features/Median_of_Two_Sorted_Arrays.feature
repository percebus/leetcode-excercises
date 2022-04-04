Feature: Median of Two Sorted Arrays
# SRC: https://leetcode.com/problems/median-of-two-sorted-arrays/
#
# Constraints:
#  * nums1.length == m
#  * nums2.length == n
#  * 0 <= m <= 1000
#  * 0 <= n <= 1000
#  * 1 <= m + n <= 2000
#  * -106 <= nums1[i], nums2[i] <= 106

  Scenario Outline: Odd-sized merged array
    Given two sorted arrays <array1> and <array2>
      And of size <m> and <n> respectively
     When I call find_median
     Then return the <median> of the two sorted arrays <merged>
#     But the overall run time complexity should be O(log (m+n)) # TODO
  Examples:
  |     array1      | m | array2 | n |      merged     | number(s) | median |
  |     [1, 3]      | 2 |  [2]   | 1 |    [1, 2, 3]    |    [2]    |      2 |
  | [1, 2, 3, 4, 5] | 5 |   []   | 0 | [1, 2, 3, 4, 5] |    [3]    |      3 |


  Scenario Outline: Median of 2 numbers in an even-sized merged array
    Given two sorted arrays <array1> and <array2>
      And of size <m> and <n> respectively
     When I call find_median
     Then return the <median> of the two sorted arrays <merged>
#     But the overall run time complexity should be O(log (m+n)) # TODO
  Examples:
  | array1 | m | array2 | n |    merged    | number(s)| median |   explanation  |
  | [1, 2] | 2 | [3, 4] | 2 | [1, 2, 3, 4] |  [2, 3]  |   2.5  | (2+3) /2 = 2.5 |


  Scenario Outline: Out of bounds
    Given two empty arrays <array1> and <array2>
      And of size <m> and <n> respectively
     Then handle the exception for two empty arrays
  Examples:
  | array1 | m | array2 | n |    merged    | number(s)| median | explanation |
  |   []   | 0 |   []   | 0 |      []      |   None   |  None  | No numbers  |
