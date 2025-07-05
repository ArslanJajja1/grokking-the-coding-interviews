#!/usr/bin/env python3
"""
palindrome.py

A simple palindrome checker that ignores non-alphanumeric characters and case.

Usage:
    python palindrome.py "A man, a plan, a canal: Panama"
    python palindrome.py "race a car"
"""

import sys

def is_palindrome(s: str) -> bool:
    """
    Check if the input string `s` is a palindrome.

    This function uses a two-pointer approach:
      - `start` moves forward from the left.
      - `end` moves backward from the right.
    It skips any characters that are not letters or digits,
    and compares characters case-insensitively.
    """
    start, end = 0, len(s) - 1

    while start < end:
        # Skip non-alphanumeric on the left
        while start < end and not s[start].isalnum():
            start += 1
        # Skip non-alphanumeric on the right
        while start < end and not s[end].isalnum():
            end -= 1

        # If the characters don't match (ignoring case), it's not a palindrome
        if s[start].lower() != s[end].lower():
            return False

        # Move both pointers inward
        start += 1
        end -= 1

    # All checks passed
    return True

def main():
    """
    Parse the command-line argument and print the result.
    Exits with usage information if no argument is provided.
    """
    if len(sys.argv) != 2:
        print("Usage: python palindrome.py \"string to check\"")
        sys.exit(1)

    input_str = sys.argv[1]
    if is_palindrome(input_str):
        print(f"✔️  '{input_str}' is a palindrome")
    else:
        print(f"❌  '{input_str}' is NOT a palindrome")

if __name__ == "__main__":
    main()


# TC = O(N)
# SC = O(1)