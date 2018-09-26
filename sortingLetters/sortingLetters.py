def sortRGB( arr):
    lo = 0
    hi = len(arr) - 1
    mid = 1
    while mid <= hi:
        if arr[mid] == 'R':
            arr[lo],arr[mid] = arr[mid],arr[lo]
            lo = lo + 1
            mid = mid + 1
        elif arr[mid] == 'G':
            mid = mid + 1
        else:
            arr[mid],arr[hi] = arr[hi],arr[mid] 
            hi = hi - 1
    return arr

arr = ['G','B','R','R','B','R','G']
arr = sortRGB( arr)
print ("Array after segregation :")
print (arr)