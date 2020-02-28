def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = round((low + high)/2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid
        else:
            low = mid
    return None


my_list = [1, 3, 5, 7, 9, 11, 12]

print(binary_search(my_list, 12))
