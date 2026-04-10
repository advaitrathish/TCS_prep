def find_duplicates(arr):
    seen = set()
    duplicates = set()
    
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
            
    return list(duplicates)

# Example usage
arr = [1, 2, 3, 4, 2, 5, 1]
print(find_duplicates(arr))  # Output: [1, 2]   

# The function `find_duplicates` takes a list of numbers as input and returns a list of duplicate numbers. It uses two sets: `seen` to keep track of numbers that have been encountered, and `duplicates` to store numbers that have been seen more than once. The function iterates through the input list, adding numbers to the `seen` set and checking for duplicates. Finally, it returns the duplicates as a list.