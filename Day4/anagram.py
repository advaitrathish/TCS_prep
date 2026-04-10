def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    
    freq1 = {}
    freq2 = {}
    
    for ch in s1:
        freq1[ch] = freq1.get(ch, 0) + 1
        
    for ch in s2:
        freq2[ch] = freq2.get(ch, 0) + 1
        
    return freq1 == freq2

# complete the function to check if two strings are anagrams of each other
# anagrams are words or phrases made by rearranging the letters of another, such as "listen" and "silent"

#optomized version using a single frequency dictionary
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    
    freq = {}
    
    for ch in s1:
        freq[ch] = freq.get(ch, 0) + 1
        
    for ch in s2:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] == 0:
            del freq[ch]
            
    return len(freq) == 0

# in this optimized version, we use a single frequency dictionary to count the occurrences of characters in the first string and then decrement the counts based on the second string. If any character from the second string is not found in the frequency dictionary or if any count becomes negative, we can immediately conclude that the strings are not anagrams. Finally, we check if the frequency dictionary is empty, which would indicate that all characters matched correctly.