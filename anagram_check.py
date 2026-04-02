#Problem 3: Check Anagram
# Question:

# Given two strings, check whether they are anagrams of each other.
# Two strings are anagrams if they contain the same characters with the same frequency.

#Example:

#Input:  listen, silent
#Output: True

#Input:  hello, world
#Output: False


# anagram_check.py

# Question:
# Check if two strings are anagrams

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# Quick length check
if len(s1) != len(s2):
    print("Output: False")

else:
    freq1 = {}
    freq2 = {}

    # Count frequency for s1
    for ch in s1:
        if ch in freq1:
            freq1[ch] += 1
        else:
            freq1[ch] = 1

    # Count frequency for s2
    for ch in s2:
        if ch in freq2:
            freq2[ch] += 1
        else:
            freq2[ch] = 1

    if freq1 == freq2:
        print("Output: True")
        
    else:
        print("Output: False")