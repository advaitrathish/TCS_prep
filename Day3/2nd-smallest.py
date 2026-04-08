arr = list(map(int, input().split()))

smallest = float('inf')
second = float('inf')

for num in arr:
    if num < smallest:
        second = smallest
        smallest = num
    elif smallest < num < second:
        second = num

if second == float('inf'):
    print("No second smallest")
else:
    print(second)

# complexity is O(n) because we traverse the array once.