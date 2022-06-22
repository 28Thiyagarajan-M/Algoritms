# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. T
# This algorithm is not suitable for large data sets as its average and worst case time complexity is quite high.

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n- i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]= arr[j+1],arr[j]
    
    return (arr)

arr  = [7,3,1,2,6]
print(bubbleSort(arr))
