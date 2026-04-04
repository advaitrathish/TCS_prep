#reversing vowels only in a string
def reverse_vowels(s):
    vowels = "AEIOUaeiou"
    s = list(s)

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] not in vowels:
            left += 1
        elif s[right] not in vowels:
            right -= 1
        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    return "".join(s)

# Example usage
s = "hello world"
result = reverse_vowels(s)
print(result)  # Output: "holle werld"


#without using list 
def reverse_vowels(s):
    vowels = "aeiouAEIOU"
    
    # Step 1: extract vowels
    extracted = [ch for ch in s if ch in vowels]
    
    # Step 2: reverse vowels
    extracted = extracted[::-1]
    
    # Step 3: rebuild string
    result = ""
    j = 0
    
    for ch in s:
        if ch in vowels:
            result += extracted[j]
            j += 1
        else:
            result += ch

    return result

#this is not efficient because string concatenation creates a new string every time. It has O(n^2) time complexity.