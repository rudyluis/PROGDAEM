import random
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
n=random.randrange(1,30)
v=random.sample(range(0,101),n)
print(v)
ordenado=selectionSort(v)
print(ordenado)



#### el selectionsort: Este algortimo separa la lista en dos partes, ordenada y no ordenada
#### algortimo de ordenacion mas habituales 
#### ordenamiento de burbuja (bubble sort)  
#### tipo de insercion (inter sort )
### combinar ordenacion (merge sort)