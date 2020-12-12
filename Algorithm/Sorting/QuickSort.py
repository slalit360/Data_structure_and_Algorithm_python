# Algorithm	                    Time Complexity	                        Space Complexity
#                       Best	        Average	        Worst	            Worst
# Quicksort	            Ω(n log(n))	    Θ(n log(n))	    O(n^2)	            O(log(n))


# Quick Sort :- O(n log(n))

def partition(lists, low, high):
    i = low - 1
    pivot = lists[high]

    for j in range(low, high):
        if lists[j] < pivot:
            i += 1
            lists[i], lists[j] = lists[j], lists[i]

    lists[i+1], lists[high] = lists[high], lists[i+1]
    return i + 1

def quick_sort(lists, low, high):
    if low < high:
        pi = partition(lists, low, high)
        quick_sort(lists, low, pi-1)
        quick_sort(lists, pi+1, high)

lists = [5, 7, 1, 8, 3, 9, 2]
quick_sort(lists, low=0, high=len(lists)-1)

print("Quick sort : ", lists)