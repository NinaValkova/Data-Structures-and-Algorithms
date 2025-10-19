# Extra memory O(k) (temp slice)
def rotate(nums, k):
    size = len(nums)

    # start = int(k) % size = 2 % 5 = 2
    start = int(k) % size

    # temp = nums[-2:] = [40, 50]
    temp = nums[-start:]

    # Shift elements to the right
    # 5-1 => 4  #2-1=> 1
    for i in range(size - 1, start - 1, -1):
        nums[i] = nums[i - start]
        # nums[4] = nums[4-2=> 2]
        # nums[3] = nums[3-2=> 1]
        # nums[2] = nums[2-2=>0]

    nums[:start] = temp


# input
# 5 2
# 10 20 30 40 50
line = input()
size, step = line.split()

nums = input().split()
# map() returns a map object, which is an iterator
nums = list(map(int, nums))

rotate(nums, step)
# 40 50 10 20 30
for num in nums:
    print(num, end=" ")
