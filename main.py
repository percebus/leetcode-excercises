from problems.hopper import categorize
from problems.leetcode import median_of_two_sorted_arrays, two_sum, summary_ranges


def main():
    two_sum.run_all()
    median_of_two_sorted_arrays.run_all()
    summary_ranges.run_all()

    categorize.run_all()


if __name__ == '__main__':
    main()
