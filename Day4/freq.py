def char_frequency(s):
    freq = {}
    
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
            
    return freq

# complexity is O(n) where n is the length of the input string, because we iterate through each character once.