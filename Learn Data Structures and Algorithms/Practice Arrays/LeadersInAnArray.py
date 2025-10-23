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
    flag = True
    leaders = []
    for i in range(0, size, 1):
        current_number = nums[i]
        for j in range(i+1, size, 1):
            if current_number <= nums[j]:
                flag = False
                break
        if flag:
            leaders.append(current_number)
        flag = True

    return leaders


size = int(input())
nums = list(map(int, input().split()))

leaders = findLeaders(size, nums)
for leader in leaders:
    print(leader, end=" ")
