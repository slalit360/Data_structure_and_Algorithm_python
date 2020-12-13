# Algorithm	                    Time Complexity	                        Space Complexity
#                       Best	        Average	        Worst	            Worst
# Quicksort	            Ω(n log(n))	    Θ(n log(n))	    O(n^2)	            O(log(n))


# Quick Sort :- O(n log(n))

def partition(array, low, high):
    i = low - 1
    pivot = array[high]

    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def partition_1(array, low, high):
    pi = low
    pivot = array[pi]

    while low < high:
        while low < len(array) and array[low] <= pivot:
            low += 1
        while array[high] > pivot:
            high -= 1
        if low < high:
            array[low], array[high] = array[high], array[low]

    array[pi], array[high] = array[high], array[pi]

    return high


def quick_sort(array, low, high):
    if low < high:
        pi = partition_1(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)


array = [5, 7, 1, 8, 3, 9, 2]
quick_sort(array, low=0, high=len(array) - 1)

print("Quick sort : ", array)
