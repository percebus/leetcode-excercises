import math


# SRC: https://leetcode.com/problems/median-of-two-sorted-arrays/
#
# Given two sorted arrays nums1 and nums2
# of size m and n respectively,
# return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)). # TODO TEST
def find_median(nums1, nums2):
    nums3 = nums1 + nums2
    nums3.sort()
    size = len(nums3)
    mid = math.ceil(size / 2)
    is_pair = (size % 2) == 0
    idx = mid - 1

    if is_pair is False:
        return nums3[idx]

    # implicit else
    return (nums3[idx] + nums3[idx + 1]) / 2


def test(nums1, nums2, expected=None):
    result = find_median(nums1, nums2)
    assert result == expected
    print('✅', end='')


def test_all():
    # Example 1:
    # - Input: nums1 = [1,3], nums2 = [2]
    # - Output: 2.00000
    # - Explanation: merged array = [1,2,3] and median is 2.
    test([1, 3], [2], expected=2)

    # Example 2:
    # - Input: nums1 = [1,2], nums2 = [3,4]
    # - Output: 2.50000
    # - Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
    test([1, 2], [3, 4], expected=2.5)

    test([1, 2, 3, 4, 5], [], expected=3)

    print('\n')


if __name__ == '__main__':
    test_all()
