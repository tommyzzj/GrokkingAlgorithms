def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        great = [i for i in array[1:] if i >= pivot]

        return quicksort(less) + [pivot] + quicksort(great)


print(quicksort([5, 6, 3, 9, 1]))
