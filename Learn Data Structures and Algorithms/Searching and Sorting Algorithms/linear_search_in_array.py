"""
Write a program to search for a specific element in an array and print "Yes" if the element is present, otherwise print "No".

Input:
The first line contains an integer 
n, the length of the array and 
k, the element to be search.
The second line contains 
n space-separated integers representing the elements of the array.
Output:
Print "Yes" if the element k is present in the array.
Print "No" if the element k is not present in the array.
"""

def isFound(length, element, nums):
    for i in range(0, length):
        if nums[i] == element:
            return True
    return False    
    

length, element = map(int, input().split(' '))
nums = list(map(int, input().split(" ")))

if isFound(length, element, nums):
    print("Yes")
else:
    print("No")    
    