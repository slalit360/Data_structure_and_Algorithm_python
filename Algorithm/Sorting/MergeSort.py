# Algorithm	                    Time Complexity	                        Space Complexity
#                       Best	        Average	        Worst	            Worst
# Quicksort	            Ω(n log(n))	    Θ(n log(n))	    O(n log(n))		    O(n)


# Merge Sort :- O(n log(n))

def merge_sorted_list(a, b, array):
    lena = len(a)
    lenb = len(b)
    i = j = k = 0

    while i < lena and j < lenb:
        if a[i] <= b[j]:
            array[k] = a[i]
            i += 1
        else:
            array[k] = b[j]
            j += 1
        k += 1

    while i < lena:
        array[k] = a[i]
        i += 1
        k += 1

    while j < lenb:
        array[k] = b[j]
        j += 1
        k += 1


def merge_sort(array):
    if len(array) == 1:
        return

    mid = len(array) // 2

    left = array[:mid]
    right = array[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_sorted_list(left, right, array)


arr = [1, 9, 2, 55, 12, 77]
merge_sort(array=arr)
print(arr)
# print(merge_sorted_list(a=[1, 3, 8], b=[2, 5, 10]))
