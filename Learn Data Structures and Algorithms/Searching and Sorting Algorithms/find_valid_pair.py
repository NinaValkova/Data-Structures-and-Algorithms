"""
Write a program that reads an integer n followed by n pairs of integers.
Given two additional integers left and right,
the program should print all pairs whose sum and product fall within the inclusive range [left, right].
"""


def readPairs(size):
    pairs = []
    for i in range(0, size):
        pair = tuple(map(int, input().split(" ")))
        pairs.append(pair)

    return pairs


def getPairs(pairs, n, left, right):
    result_pairs = []
    for first, second in pairs:
        sum = first + second
        product = first * second

        if (sum >= left and sum <= right) and (product >= left and product <= right):
            result_pairs.append((first, second))

    return result_pairs


n = int(input())
pairs = readPairs(n)
left, right = map(int, input().split(" "))
result_pairs = getPairs(pairs, n, left, right)
for first, second in result_pairs:
    print(f"{first} {second}")


# n = int(input())

# pairs = []
# for _ in range(n):
#     pair = tuple(map(int, input().split()))
#     pairs.append(pair)

# left, right = map(int, input().split())

# # Output pairs whose sum and product are within [left, right]
# for a, b in pairs:
#     if left <= a + b <= right and left <= a * b <= right:
#         print(a, b)
