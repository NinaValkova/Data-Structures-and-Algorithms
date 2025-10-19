# Given an array A of size N, your task is to find and print all the peak elements in the array.
# A peak element is one that is strictly greater than its neighboring elements.
# For the first and last elements, only consider their single adjacent element.
# If no peak element exists in the array, print -1.

# Input
# 5
# 1 2 4 3 1
# Output
# 4


def FindElements(nums, size):
    elements = []

    if size == 1:
        return [nums[0]]

    if nums[0] > nums[1]:
        elements.append(nums[0])

    for i in range(1, size - 1):
        if nums[i] > nums[i + 1] and nums[i] > nums[i - 1]:
            elements.append(nums[i])

    if nums[size - 1] > nums[size - 2]:
        elements.append(nums[size - 1])

    if not elements:
        return [-1]

    return elements


size = int(input())
nums = list(map(int, input().split()))
# elements = FindElements(nums, size)
# for element in elements:
#     print(element, end=' ')


elements = [
    nums[i]
    for i in range(size)
    if (i == 0 or nums[i] > nums[i - 1]) and (i == size - 1 or nums[i] > nums[i + 1])
]

if elements:
    print(" ".join(map(str, elements)))
else:
    print("-1")
