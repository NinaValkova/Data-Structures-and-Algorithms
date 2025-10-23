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

# Bubble Sort
# Time Complexity: O(n²)
# Space Complexity: O(1) (it sorts in place)
def sortNums(nums, size):
    for i in range(0, size, 1):
        for j in range(0, size-i-1, 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

# Time Complexity: O(n)
# Space Complexity: O(1)
def findLongestConsecutiveNumbers(nums, size):
    counter = 1
    max_counter = -1
    for i in range(0, size-1, 1):
        if nums[i + 1] == nums[i]:
            continue
        if nums[i+1]-nums[i] == 1:
            counter+=1
        else:
            counter = 0
        if max_counter < counter:
            max_counter = counter   

    return max_counter         


size = int(input())
nums = list(map(int, input().split()))

sortNums(nums, size)
print(nums)
max_counter = findLongestConsecutiveNumbers(nums, size)
print(max_counter)
