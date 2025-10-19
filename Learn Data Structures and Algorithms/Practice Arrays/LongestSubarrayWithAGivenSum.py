# Time Brute-force O(n²) - nested loop makes it O(n²)
# Space: O(1) — only a few variables used.

# You are given an array of integers nums with length n 
# and an integer k. 
# Your task is to determine the length of the longest continuous
# sub-array whose elements sum up exactly to k. 
# If there is no such sub-array, return 0.

# Input
# 6 15
# 10 5 2 7 1 9
# Output
# 4
def longestSubarraySum(nums, k):
    sum = 0
    size = len(nums)
    counter = 0
    max_counter = 0
    for j in range(0, size, 1):
        for i in range(j, size, 1):
            sum += nums[i]
            counter += 1

            if sum == k:
                if max_counter < counter:
                    max_counter = counter
                    counter = 0
                    sum = 0
            elif sum > k:
                counter = 0
                sum = 0
        counter = 0
        sum = 0

    return max_counter


size = int(input())
for i in range(0, size, 1):
    line = input()
    length, sum = line.split()
    sum = int(sum)
    nums = input().split()
    nums = list(map(int, nums))
    longest_length = longestSubarraySum(nums, sum)
    print(longest_length)
