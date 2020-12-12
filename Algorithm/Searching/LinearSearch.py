# linear Search : O(n)

def search(number_list, number_to_search):
    for i in range(0, len(number_list)):
        if number_list[i] == number_to_search:
            print(f"Element {number_to_search} is present at index : ", i)
            return i
    else:
        print(f"Element {number_to_search} is not present in array")


number_list = [2, 3, 4, 10, 40]
result = search(number_list, number_to_search=10)
result = search(number_list, number_to_search=150)