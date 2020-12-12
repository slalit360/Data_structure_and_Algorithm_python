# Binary search :- O(log(n))

def binarySearch(ls, low, high, element):
    if low <= high:
        mid = (low + high) // 2

        if ls[mid] == element:
            return f"Element found at : {mid} index"
        elif ls[mid] > element:
            return binarySearch(ls, low, mid - 1, element)
        else:
            return binarySearch(ls, mid + 1, high, element)
    else:
        return f"Element {element} not found (-1)"


sorted_list = [1, 2, 3, 5, 7, 8, 9]
print(binarySearch(sorted_list, low=0, high=len(sorted_list) - 1, element=7))
