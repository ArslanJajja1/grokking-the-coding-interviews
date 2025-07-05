#!/usr/bin/env python3
"""
three_sum.py

Find all unique triplets in an integer array that sum to zero.

Usage:
    python three_sum.py "[-1, 0, 1, 2, -1, -4]"
"""

import sys
import ast

def three_sum(nums):
    """
    Returns a list of lists, where each
    inner list is a triplet [a, b, c] such that:
      - a + b + c == 0
      - triplets are unique (no duplicate permutations)
    """
    nums.sort()  # sort to make two-pointer de-dup logic work
    res = []

    for i in range(len(nums) - 2):
        # If the current value is the same as the one before, skip it
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Two-pointer scan for pairs that sum with nums[i] to zero
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                res.append([nums[i], nums[left], nums[right]])
                left  += 1
                right -= 1

                # Skip duplicates on the left
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                # Skip duplicates on the right
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < 0:
                # Need a larger sum: move left pointer right
                left += 1
            else:
                # Need a smaller sum: move right pointer left
                right -= 1

    return res


def main():
    """
    Parse the single command-line argument as a Python list of ints,
    run three_sum, and print the results.
    """
    if len(sys.argv) != 2:
        print("Usage: python three_sum.py \"[num1, num2, num3, ...]\"")
        sys.exit(1)

    try:
        nums = ast.literal_eval(sys.argv[1])
        if not isinstance(nums, list):
            raise ValueError
    except Exception:
        print("Error: argument must be a Python list of integers, e.g. \"[-1,0,1,2,-1]\"")
        sys.exit(1)

    triplets = three_sum(nums)
    print("Input:   ", nums)
    print("Triplets:", triplets)


if __name__ == "__main__":
    main()
