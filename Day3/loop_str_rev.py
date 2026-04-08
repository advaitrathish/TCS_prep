s = input()
rev = ""
for char in s:
    rev = char + rev
print(rev)

#Can also be done using slicing
s = input()
rev = s[::-1]
print(rev)