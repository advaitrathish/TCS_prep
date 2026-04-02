# Problem 5: Count Words in a Sentence
# Question:

# Given a sentence (string), count the number of words in it.

#Conditions:
# A word is a sequence of characters separated by spaces
# Ignore multiple spaces
# Do not use built-in functions like split()

# Examples: 
# Input:  "Hello world" 
# Output: 2 
# Input:  "  I   love   coding  " 
# Output: 3 Input:  ""
# Output: 0


# count_words.py

# Question:
# Count number of words in a sentence without using split()

s = input("Enter a sentence: ")

count = 0

for i in range(len(s)):
    if s[i] != ' ':
        if i == 0 or s[i-1] == ' ':
            count += 1

print("Output:", count)