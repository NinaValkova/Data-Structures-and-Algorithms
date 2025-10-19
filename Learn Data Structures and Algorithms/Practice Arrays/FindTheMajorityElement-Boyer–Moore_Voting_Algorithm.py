# You are given an array arr containing n integers.
# Your task is to return the majority element.

# A majority element is defined as the element that occurs
# more than ⌊n / 2⌋ times. It is guaranteed that such an element
# always exists.

# Boyer–Moore Voting Algorithm,
# algorithms to find the majority element in an array
# — O(n) time and O(1) space.


# majority element is the element that appears more than n/2 times
# The true majority element will survive all cancellations because it occurs more than all others combined.
# Each element can "vote" for itself.
# If another element shows up, it cancels one vote from the current candidate.
def majorityElement(arr):
    occurrences = 0
    majorityElement = arr[0]

    for number in arr:
        if number == majorityElement:
            occurrences += 1
        else:
            occurrences -= 1
            if occurrences == 0:
                majorityElement = number
                occurrences = 1

    return majorityElement


size = int(input())
nums = list(map(int, input().split()))
max_occurrences = majorityElement(nums)
print(max_occurrences)
