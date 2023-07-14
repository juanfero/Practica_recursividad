#Juan Felipe Rojas.
# Ejercicio practico recursividad. 



def sum_arrays_recursive(array1, array2, i, result):
    if i == len(array1):
        return result
    result.append(array1[i] + array2[i])
    return sum_arrays_recursive(array1, array2, i + 1, result)

def sum_arrays_iterative(array1, array2):
    result = []
    for i in range(len(array1)):
        result.append(array1[i] + array2[i])
    return result

def sum_array_elements(array):
    result = 0
    for i in range(len(array)):
        result += array[i]
    return result

array1 = []
array2 = [5, 4, 3, 2, 1]

array3 = sum_arrays_recursive(array1, array2, 0, [])
print("Array 3 (recursive):", array3)

array3 = sum_arrays_iterative(array1, array2)
print("Array 3 (iterative):", array3)

sum1 = sum_array_elements(array1)
print("Sum of Array 1:", sum1)

sum2 = sum_array_elements(array2)
print("Sum of Array 2:", sum2)

# Ordenar el arreglo
my_list = [1, 7, 4, 5, 9, 8]
result = sorted(my_list)
print(result)
