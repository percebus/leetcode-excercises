

# Reverse to Make Equal
#
# Signature
#   bool areTheyEqual(int[] arr_a, int[] arr_b)
#
# Output: Return true if B can be made equal to A, return false otherwise.
def are_they_similar(array_a: list, array_b: list) -> bool:
    if array_a == array_b:
        return True

    length_a = len(array_a)
    lenght_b = len(array_b)
    if length_a != lenght_b:
        raise Exception(f'mismtaching lengths: {length_a} VS {lenght_b}')

    for i in range(length_a):
        left = array_b[:i]
        for j in range(i + 1, lenght_b):
            mid = array_b[i: j + 1]
            right = array_b[j + 1: lenght_b]
            inverted = mid[::-1]
            new_array = left + inverted + right
            if array_a == new_array:
                return True

    return False


def test(array_a: list, array_b: list, expected: bool = None):
    result = are_they_similar(array_a, array_b)
    assert result == expected, f'expected:{expected}, got:{result}'
    print('✅', end='')


def test_all():
    # Example
    #   A = [1, 2, 3, 4]
    #   B = [1, 4, 3, 2]
    #
    # output = true
    #
    # Explanation
    # After reversing the subarray of B from indices 1 to 3,
    # array B will equal array A.
    test([1, 2, 3, 4], [1, 4, 3, 2], expected=True)

    print('\n')


if __name__ == '__main__':
    test_all()
