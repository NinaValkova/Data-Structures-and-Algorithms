"""
Given a string and a character as input,
print the first position of the character in the string if it is present.
If the character does not exist in the string, print "-1".

Input
HelloHowYouDoing
w
Output
7
"""

def getIndex(word, character):
    for i, c in enumerate(word):
        if c == character:
            return i
    return -1    
             
        
word = input()
character = input() 

index = getIndex(word, character)
print(index)