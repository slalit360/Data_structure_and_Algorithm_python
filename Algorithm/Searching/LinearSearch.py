# linear Search : O(n)

def search(arr, n, x):
    for i in range(0, n):
        if arr[i] == x:
            return i
    return -1


arr = [2, 3, 4, 10, 40]
result = search(arr, n=len(arr), x=10)
if (result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)
