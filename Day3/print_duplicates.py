arr = list(map(int, input().split()))
duplicates = []
distinct = []

for num in arr:
    if num in distinct:
        if num not in duplicates:
            duplicates.append(num)
    else:
        distinct.append(num)

print(duplicates)

# complexity is O(n) because we traverse the array once.

# next we can also use set to find duplicates more efficiently
arr = list(map(int, input().split()))
seen = set()
duplicates = set()
for num in arr:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print(list(duplicates))

# complexity is O(n) because we traverse the array once and set operations are O(1) on average.