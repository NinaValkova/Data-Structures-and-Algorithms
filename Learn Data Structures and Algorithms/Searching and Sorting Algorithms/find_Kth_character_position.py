"""
Given a string s1, a character c1, and an integer k, find and print the position of the
kth occurrence of the character c1 in the string s1.
If the kth occurrence does not exist, print -1.
"""


def getPosition(word, character, num):
    occurance = 0
    for i, c in enumerate(word):
        if c == character:
            occurance += 1
            if occurance == num:
                return i
    return -1    


word, character, num = input().split(" ")
num = int(num)

index = getPosition(word, character, num)
print(index)

# s1, c1, k = input().split()
# k = int(k)

# count = 0
# for i, char in enumerate(s1):
#     if char == c1:
#         count += 1
#         if count == k:
#             print(i)
#             break
# else:
#     print(-1)
