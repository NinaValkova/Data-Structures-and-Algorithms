"""You are given an integer array nums.
An element in the array is called a leader
if it is strictly larger than every element to its right.
The last element in the array is always considered a leader.

Sample Input
6
10 7 8 3 5 2
Your Output
10 8 5 2

"""


def findLeaders(size, nums):
    size = len(nums)
    leaders = []
    # largest number we’ve seen so far
    max_from_right = nums[-1]
    leaders.append(max_from_right)

    for i in range(size - 2, -1, -1):
        if nums[i] > max_from_right:
            leaders.append(nums[i])
            max_from_right = nums[i]

    leaders.reverse()
    return leaders


size = int(input())
nums = list(map(int, input().split()))

leaders = findLeaders(size, nums)
for leader in leaders:
    print(leader, end=" ")
