# You are given an array arr containing n integers.
# Your task is to return the majority element.

# A majority element is defined as the element that occurs
# more than ⌊n / 2⌋ times. It is guaranteed that such an element
# always exists.

# brute-force nested loop (O(n²)) version


def majorityElement(arr, size):
    occurrences = 0
    max_occurrences = -1
    element = 0
    majorityElement = 0
    for i in range(0, size, 1):
        element = arr[i]
        for j in range(0, size, 1):
            if element == arr[j]:
                occurrences += 1
        if max_occurrences < occurrences:
            max_occurrences = occurrences
            majorityElement = element
        occurrences = 0

    return majorityElement


size = int(input())
nums = list(map(int, input().split()))
max_occurrences = majorityElement(nums, size)
print(max_occurrences)
