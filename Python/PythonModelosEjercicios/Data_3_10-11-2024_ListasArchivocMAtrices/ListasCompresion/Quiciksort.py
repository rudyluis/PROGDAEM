import random
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for x in arr[1:]:
            if x < pivot:
                left.append(x)
            else:
                right.append(x)
        return quickSort(left) + [pivot] + quickSort(right)


n=random.randrange(1,30)

v=random.sample(range(0,101),n)
print(v)
ordenado=quickSort(v)
print(ordenado)