# Selection sort is used for small arrays.
# Time Complexity: The time complexity of Selection Sort is O(N2) as there are two nested loops.
# arr = [23,35,78,34,12]
# 1st iteration,
# arr = [12,35,78,34,23]
# 2nd iteration,
# arr = [12,23,78,34,35]
# 3rd iteration,
# arr = [12,23,34,78,35]
# 4th iteration,
# arr= [12,23,34,35,78]

arr = [23,35,78,34,12]
print("Original Array: ", *arr)
#Accending Order
for i in range(0, len(arr)):
    for j in range(i,len(arr)):
        if(arr[i]>arr[j]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print("Accending Order: ",*arr)

#Decending Order
for i in range(0, len(arr)):
    for j in range(i,len(arr)):
        if(arr[i]<arr[j]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print("Deccending Order: ",*arr)