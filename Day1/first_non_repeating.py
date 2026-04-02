#Problem 2: First Non-Repeating Character
# Question:

# Given a string, find the first character that does not repeat.
# If all characters repeat, return -1.

#Example:

#nput:  aabbcde
#Output: c

#Input:  aabbcc
#Output: -1


# first_non_repeating.py

# Question:
# Find the first non-repeating character in a string

s = input("Enter a string: ")

freq = {}

# Count frequency
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

# Find first non-repeating
for ch in s:
    if freq[ch] == 1:
        print("Output:", ch)
        break
else:
    print("Output: -1")