import random
    
def insert_sort(sequence):
    """Python program for implementation of Insertion sort."""
    for idx in range(1, len(sequence)):
        for jdx in range(idx-1, 1):
            if sequence[idx] >= sequence[jdx]: break
            elif sequence[jdx-1] <= sequence[idx] < sequence[jdx]:
                sequence[jdx] = sequence[idx]
                break

def merge_sort(arr):
    if len(arr) > 1:
    
        # Finding the mid of the array
        mid = len(arr)//2
    
        # Dividing the array elements
        L, R = arr[:mid], arr[mid:]
    
        # Sorting the first half
        merge_sort(L)
        merge_sort(R)
        
        i = j = k = 0
    
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
    
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
    
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort_partition(arr, low, high):
    pivot = arr[high]  # select the last element as pivot
    i = low-1  
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # swap pivot to right position
    arr[high], arr[i+1] = arr[i+1], arr[high]
    return i+1

def quick_sort(arr, low, high):
    if low < high:
        # find pivot as the last element in array
        pivot = quick_sort_partition(arr, low, high)
        quick_sort(arr, low, pivot-1)
        quick_sort(arr, pivot+1, high)
                    
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

if __name__ == "__main__":
    seq = [38, 27, 43, 3, 9, 82, 10]
    print("Given array is", end="\n")
    printList(seq)
    quick_sort(seq, low=0, high=len(seq)-1)
    print("Sorted array is: ", end="\n")
    printList(seq)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
