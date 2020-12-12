# Binary search :- O(log(n))
# works only on sorted input list

def binarySearchRecursive(number_list, low=None, high=None, number_to_search=None):
    if low is None:
        low = 0
    if high is None:
        high = len(number_list) - 1

    if low <= high:
        mid = (low + high) // 2

        if number_list[mid] == number_to_search:
            return f"Element {number_to_search} found at index : {mid}"
        elif number_list[mid] > number_to_search:
            return binarySearchRecursive(number_list, low, mid - 1, number_to_search)
        else:
            return binarySearchRecursive(number_list, mid + 1, high, number_to_search)
    else:
        return f"Element {number_to_search} not found (-1)"

number_list = [1, 2, 3, 5, 7, 8, 9]
print(binarySearchRecursive(sorted(number_list), number_to_search=3))
print(binarySearchRecursive(sorted(number_list), number_to_search=34))


def binarySearchNonrecursive(number_list, number_to_search=None):
    low = 0
    high = len(number_list) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2

        if number_list[mid] == number_to_search:
            return f"Element {number_to_search} found at index : {mid}"
        elif number_list[mid] > number_to_search:
            high = mid - 1
        else:
            low  = mid + 1

    return f"Element {number_to_search} not found (-1)"


number_list = [1, 2, 3, 5, 7, 8, 9]
print(binarySearchNonrecursive(sorted(number_list), number_to_search=3))
print(binarySearchNonrecursive(sorted(number_list), number_to_search=34))
