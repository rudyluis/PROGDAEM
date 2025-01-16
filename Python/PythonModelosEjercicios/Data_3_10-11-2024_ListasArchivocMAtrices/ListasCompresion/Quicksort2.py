def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

# Ejemplo de uso
my_list = [36, 61, 8, 100, 52, 42, 20]
sorted_list = quicksort(my_list)
print(sorted_list)

 