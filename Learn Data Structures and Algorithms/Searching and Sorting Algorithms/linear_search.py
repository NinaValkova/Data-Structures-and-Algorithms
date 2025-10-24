# Linear search, also known as sequential search,
# is a simple searching algorithm that checks each element
# in a list one by one until the desired element is found or the list ends.

# How Linear Search Works:
# 1. Start from the first element of the list.
# 2. Compare the current element with the target element.
# 3. If a match is found, return the position.
# 4. If no match, move to the next element.
# 5. Repeat until the target is found or the end of the list is reached.
# 6. If the target is not found, the search is unsuccessful.


"""
Given the program to check 7 is present or not, print Yes if 7 is present in the array.
Analyze the code for linear search and submit.
"""

# Define the array
array = [3, 5, 2, 9, 7, 1]
found = False

# Check if 7 is present in the array
for element in array:
    if element == 7:
        found = True
        break

# Print the result
if found:
    print("Yes")
else:
    print("No")
