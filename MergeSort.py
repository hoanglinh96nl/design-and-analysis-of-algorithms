def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr)//2
        left, right = arr[:middle], arr[middle:]
        
        merge_sort(left)
        merge_sort(right)
        
        i = j = k = 0
        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1 
            else:
                arr[k] = right[j]
                j += 1 
            k += 1  # update next smallest element in sub-arrays
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            
arr = [9,8,7,6,5,4,3,2,1]
merge_sort(arr)
print(arr)