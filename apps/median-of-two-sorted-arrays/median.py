import math


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


def main():
    # TODO accept args
    result = find_median([1, 2, 3, 4, 5], [])
    print(result)


if __name__ == "__main__":
    main()
