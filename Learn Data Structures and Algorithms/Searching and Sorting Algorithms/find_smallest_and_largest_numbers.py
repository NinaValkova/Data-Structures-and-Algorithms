"""
Write a program to find the smallest and largest elements in an array of integers.

Input
10
4 3 53 13 2 44 55 35 56 34
Output
2 56
"""

def getValues(size, nums):
    # float('inf') acts like “larger than any finite number”.
    smallest = float("inf")
    biggest = float("-inf")
    
    for num in nums:
        if num < smallest:
            smallest = num
        if num > biggest:
            biggest = num
            
    return smallest, biggest            


size = int(input())
nums = list(map(int, input().split(" ")))

smallest, biggest = getValues(size, nums)
print(f"{smallest} {biggest}")