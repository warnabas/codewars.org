def binarySearch (arr, left, right, x): 
    
    if right >= left: 
  
        mid = left + (right - left)/2
  
       	if arr[mid] == x: 
            return mid 
          
        elif arr[mid] > x: 
            return binarySearch(arr, left, mid-1, x) 
  
        else: 
            return binarySearch(arr, mid+1, right, x) 
  
    else: 
        
        return -1
  
arr = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17 ] 
x = 10
  
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print "Element is present at index %d" % result 
else: 
    print "Element is not present in array"