# Time: O(n) — single pass
# Space: O(n) — stores prefix sums in a dictionary

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
    # prefix sum is the sum of all elements from the beginning of the array up to the current index.
    prefix_sum = 0
    max_counter = 0
    # dictionary (hashmap) that records the first time each prefix sum appears.
    prefix_index = {}

    for i, num in enumerate(nums):
        prefix_sum += num

        # handles subarrays starting at 0.
        # prefix_sum for all iterations - 1, 3, 6, 8, 9
        if prefix_sum == k:
            max_counter = i + 1

        # handles subarrays starting anywhere else.
        # Tests whether removing an earlier prefix makes current subarray sum to k
        # There is no subarray ending at index 4 that sums to 5. - 4 exist as a key? ❌ No
        # but At i=2 prefix_sum - k = 6 - 5 = 1 and 1 in prefix_index; 1 exists at index 0 → j = 0
        if (prefix_sum - k) in prefix_index:
            # Formula: subarray that sums to k is from j+1 to i
            # Subarray starts after index 0 → index 1
            # Subarray ends at current index i = 2 {1:0, 3:1, 6:2, 8:3, 9:4}
            # i - prefix_index[1] = 2 - 0 = 2 update max length
            max_counter = max(max_counter, i - prefix_index[prefix_sum - k])

        # index stores the first index where a particular sum occurs.
        # Dictionary storing the first index where each prefix sum appeared {1:0, 3:1, 6:2, 8:3, 9:4} for each sum i got index when appears
        # 1 is in prefix_index at index 0. - There exists a previous prefix sum = 1 at index 0.
        if prefix_sum not in prefix_index:
            prefix_index[prefix_sum] = i

    return max_counter


line = input()
# 6 5
length, sum = line.split()
sum = int(sum)

# 1, 2, 3, 2, 1
nums = input().split()
nums = list(map(int, nums))

longest_length = longestSubarraySum(nums, sum)
print(longest_length)
