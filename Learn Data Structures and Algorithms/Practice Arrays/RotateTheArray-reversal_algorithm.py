# Extra memory O(1)
def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


def rotate(nums, k):
    size = len(nums)

    # # int("7") % 5 = 7 % 5 = 2 - Rotating by 7 steps is the same as rotating by 2 steps, because every 5 steps brings the list back to its start.
    k = int(k) % size

    # 10 20 30 40 50
    reverse(nums, 0, size - 1)
    # 50 40 30 20 10
    reverse(nums, 0, k - 1)
    # 40 50 30 20 10
    reverse(nums, k, size - 1)


# input
# 5 2
# 10 20 30 40 50
line = input()
size, step = line.split()
step = int(step)

nums = input().split()
# map() returns a map object, which is an iterator
nums = list(map(int, nums))

rotate(nums, step)
# 40 50 10 20 30
for num in nums:
    print(num, end=" ")
