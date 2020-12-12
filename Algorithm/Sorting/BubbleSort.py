# Algorithm	                    Time Complexity	                        Space Complexity
#                       Best	        Average	        Worst	            Worst
# Bubble Sort	        Ω(n)	        Θ(n^2)	        O(n^2)	            O(1)

# Bubble Sort : – O(n^2)

lists = [5, 7, 1, 8, 3, 9, 2]

def bubble_sort(ls):
    n = len(ls) - 1

    for i in range(n):
        for j in range(n-i):
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]
    return ls

print("Bubble sort : ", bubble_sort(lists))