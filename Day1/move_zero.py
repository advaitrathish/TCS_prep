#Problem 1: Move Zeros to End

# Question:
# Given an array of integers, move all zeros to the end of the array while maintaining the relative order of non-zero elements.

# Example:
# Input:  0 1 0 3 1
# Output: 1 3 12 0 0

# move_zeros.py
arr = list(map(int, input("Enter numbers separated by space: ").split()))

k = 0

# Move non-zero elements to front
for i in range(len(arr)):
    if arr[i] != 0:
        arr[k] = arr[i]
        k += 1

# Fill remaining with zeros
for i in range(k, len(arr)):
    arr[i] = 0

print("Output:", arr)