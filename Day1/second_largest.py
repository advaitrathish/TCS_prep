#Problem 4: Second Largest Element
#Question:

#Given an array of integers, find the second largest element in the array.

#Conditions:
#Do not sort the array
#If second largest does not exist, return -1

# Examples:
# Input:  10 20 4 45 99
# Output: 45
# Input:  5 5 5
# Output: -1
# Input:  7
# Output: -1


# second_largest.py

# Question:
# Find the second largest element without sorting

arr = list(map(int, input("Enter numbers separated by space: ").split()))

largest = float('-inf')
second = float('-inf')

for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

if second == float('-inf'):
    print("Output:", -1)
else:
    print("Output:", second)