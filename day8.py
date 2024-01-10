import math

def is_fib(n):
    expr1 = 5 * n**2 + 4
    expr2 = 5 * n**2 - 4
    return math.isqrt(expr1)**2 == expr1 or math.isqrt(expr2)**2 == expr2

print(is_fib(8))  
print(is_fib(15)) 

# q2

def merge_sort(arr1, arr2):
    merged_arr = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        else:
            merged_arr.append(arr2[j])
            j += 1
    while i < len(arr1):
        merged_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged_arr.append(arr2[j])
        j += 1
    return merged_arr

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
   