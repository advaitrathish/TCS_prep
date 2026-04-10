def is_palindrome(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
        
    return True

# complexity is O(n) where n is the length of the input string, because in the worst case we need to compare each character once.
# Note: This function assumes that the input string is case-sensitive and does not ignore spaces or punctuation. Depending on the requirements, additional preprocessing may be needed to handle those cases.