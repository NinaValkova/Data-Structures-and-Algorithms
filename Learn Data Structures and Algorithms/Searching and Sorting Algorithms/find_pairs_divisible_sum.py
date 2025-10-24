"""
Write a program to find and print all pairs of integers
from a list of n pairs where the sum of each pair is divisible by k.
"""

def readPairs(pairs_count):
    pairs = []
    for i in range(0, pairs_count):
        pair = tuple(map(int, input().split(" ")))
        pairs.append(pair)
    return pairs    

def getPairs(pairs, divisor): 
    result_pairs = []
    for first, second in pairs:
        sum = first+second
        if sum % divisor == 0:
            result_pairs.append((first, second))

    return result_pairs


pairs_count, divisor = map(int, input().split(" "))
pairs = readPairs(pairs_count)
result_pairs = getPairs(pairs, divisor)
for first, second in result_pairs: 
    print(f"({first}, {second})")


# def main():
#     n, k = map(int, input().split())

#     pairs = []

#     for _ in range(n):
#         first, second = map(int, input().split())
#         pairs.append((first, second))

#     for first, second in pairs:
#         if (first + second) % k == 0:
#             print(f"({first}, {second})")


# if __name__ == "__main__":
#     main()
