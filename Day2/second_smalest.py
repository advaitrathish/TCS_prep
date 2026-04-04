#using sorting to find second smallest element in an array
def second_min(arr):
    arr = list(set(arr))   # remove duplicates
    
    if len(arr) < 2:
        return None
    
    arr.sort()
    return arr[1]
# Example usage
arr = [5, 3, 1, 4, 2]
result = second_min(arr)
print(result)  # Output: 2
#using linear scan to find second smallest element in an array
def second_min(arr):
    if len(arr) < 2:
        return None
    
    min1 = float('inf')
    min2 = float('inf')
    
    for num in arr:
        if num < min1:
            min2 = min1
            min1 = num
        elif min1 < num < min2:
            min2 = num
            
    return min2 if min2 != float('inf') else None
# Example usage
arr = [5, 3, 1, 4, 2]
result = second_min(arr)
print(result)  # Output: 2
# The linear scan method has O(n) time complexity and O(1) space complexity,
# while the sorting method has O(n log n) time complexity and O(n) space complexity
# due to the sorting algorithm.