def binarySearch (arr, x): 
    start = 0
    end = len(arr)
    
    while start < end: 

    	mid = (end+start)//2 

    	if arr[mid] == x: return mid 
    	elif arr[mid] > x: end = mid
    	else: start = mid +1

    return -1
  
arr = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17 ] 
x = 10
  
result = binarySearch(arr, x)
  
if result != -1: 
    print ("Element is present at index %d" % result) 
else: 
    print ("Element is not present in array")