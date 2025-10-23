"""
You are given an array of integers.
The task is to find the length of the longest sequence
of consecutive integers that can be formed from the numbers
in the array.

The sequence does not need to follow the
original order in the array.
Duplicates should not break the sequence.

Sample Input
3
5
15 12 14 16 13
7
50 3 2 1 4 9 6
6
100 300 101 103 102 105
Your Output
5
4
4
"""

# 1. Insert all numbers into a set (to allow O(1) lookups).

# 2. Iterate through the set:

# 3. For each number, check if it is the start of a sequence (i.e., num - 1 is not in the set).
# If it is, keep extending the sequence (num + 1, num + 2, …) until it breaks.
# Track the length of the sequence.
# Return the maximum length.

# The hash set approach is optimal (O(n)),
# using the idea of only starting from sequence beginnings


def findLongestConsecutiveNumbers(nums, size):
    max_counter = 0
    nums_set = set(nums)

    for num in nums_set:
        # start sequence if number before num-1 is not in nums_set
        if num - 1 not in nums_set:
            current = num
            current_counter = 1

            while current + 1 in nums_set:
                current += 1
                current_counter += 1

            max_counter = max(current_counter, max_counter)

    return max_counter


size = int(input())
nums = list(map(int, input().split()))

max_counter = findLongestConsecutiveNumbers(nums, size)
print(max_counter)
