"""
Write a program to find the element in an array with the smallest absolute difference
from a given integer k. If there are multiple elements with the same minimum difference,
print the smallest of these elements.
"""

def getMinDifference(size, number, nums):
    min_difference = float("inf")
    curr_difference = 0
    for i in range(0, size):
        curr_difference = abs(nums[i] - number)
        if curr_difference < min_difference:
            min_difference = curr_difference

    return min_difference


def getNumber(size, number, nums):
    found_numbers = []
    min_difference = getMinDifference(size, number, nums)
    curr_difference = 0
    for i in range(0, size):
        curr_difference = abs(nums[i] - number)
        if curr_difference == min_difference:
            found_numbers.append(nums[i])

    return min(found_numbers)


size, number = map(int, input().split(" "))
nums = list(map(int, input().split(" ")))

number = getNumber(size, number, nums)
print(number)


# n, k = map(int, input().split())
# arr = list(map(int, input().split()))

# min_diff = float("inf")
# result = float("inf")

# for num in arr:
#     diff = abs(num - k)
#     if diff < min_diff or (diff == min_diff and num < result):
#         min_diff = diff
#         result = num

# print(result)
