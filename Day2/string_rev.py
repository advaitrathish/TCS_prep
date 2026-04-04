#1 string concatination
s = "hello"
reversed_s = ""

for i in range(len(s) - 1, -1, -1):
    reversed_s += s[i]

print(reversed_s)
#string concatination is inefficient because it creates a new string every time we concatenate. 



#2 List method 
s = "hello"
res = []

for i in range(len(s) - 1, -1, -1):
    res.append(s[i])

reversed_s = "".join(res)
#join is more efficient because it creates a single string from the list of characters.



#3 python has a built-in function to reverse a string using slicing
s = "hello"
reversed_s = s[::-1]
print(reversed_s)
#slicing is the most efficient way to reverse a string in Python because it is implemented in C and optimized for performance.