

def reformat(serie):
    first = str(serie[0])
    last = str(serie[-1])
    return first if first == last else '->'.join([first, last])


# SRC: https://leetcode.com/problems/summary-ranges/
#
# You are given a sorted unique integer array nums.
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
# That is, each element of nums is covered by exactly one of the ranges,
# and there is no integer x such that x is in one of the ranges but not in nums.
#
# Each range [a,b] in the list should be output as:
#  * "a->b" if a != b
#  * "a" if a == b
def summary_ranges(nums):
    serie = []
    series = []
    for idx, value in enumerate(nums):
        if serie and (value -1) == nums[idx - 1]:
            serie.append(value)
        else:
            serie = [value]
            series.append(serie)

    result = map(reformat, series)
    return list(result)


def test(nums, expected=None):
    result = summary_ranges(nums)
    print(result)
    assert result == expected


def test_all():
    # Example:
    #  - Input: nums = [0,1,2,4,5,7]
    #  - Output: ["0->2","4->5","7"]
    test([0, 1, 2, 4, 5, 7], expected=['0->2', '4->5', '7'])

    # Example 2:
    # - Input: nums = [0, 2, 3, 4, 6, 8, 9]
    # - Output: ["0", "2->4", "6", "8->9"]
    test([0, 2, 3, 4, 6, 8, 9], expected=['0', '2->4', '6', '8->9'])


if __name__ == '__main__':
    test_all()
