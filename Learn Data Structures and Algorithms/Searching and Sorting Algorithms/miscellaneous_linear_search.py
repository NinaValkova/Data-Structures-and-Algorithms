"""
Given n pairs of integers,
write a program to check if there exists any pair that contains both integers a and b in any order.


Input Format
The first line contains an integer n, the number of pairs.
The next n lines each contain two space-separated integers representing a pair.
The last line contains two integers a and b.

Output Format
Print "Yes" if there exists any pair that contains both integers a and b in any order.
Print "No" if no such pair exists.

Input
4
2 3
4 5
3 5
1 7
5 3

Output
Yes
"""
def readPairs(n):
    pairs = []
    for i in range(0, n):
        num_1, num_2 = map(int, input().split(" "))
        pairs.append((num_1, num_2))
    return pairs

def isFound(n, pairs, pair):
    for i in range(0, n):
        num_1, num_2 = pairs[i]
        if (num_1 == pair[0] and num_2 == pair[1]) or (num_1 == pair[1] and num_2 == pair[0]):
            return True
    return False    


n = int(input())
pairs = readPairs(n)
pair = tuple(map(int, input().split(" ")))

if isFound(n, pairs, pair):
    print("Yes")
else:
    print("No")    


# # Read the number of pairs
# n = int(input())

# # Read the pairs
# pairs = []
# for _ in range(n):
#     pair = tuple(map(int, input().split()))
#     pairs.append(pair)

# # Read the integers a and b
# a, b = map(int, input().split())

# # Initialize a flag to indicate if the pair is found
# found = False

# # Check each pair
# for x, y in pairs:
#     if (x == a and y == b) or (x == b and y == a):
#         found = True
#         break

# # Print the result
# if found:
#     print("Yes")
# else:
#     print("No")
