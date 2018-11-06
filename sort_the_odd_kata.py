# You have an array of numbers.
# Your task is to sort ascending odd numbers but even numbers 
# must be on their places.

# Zero isn't an odd number and you don't need to move it. 
# If you have an empty array, you need to return it.

# Example

# sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
def sort_array(arr):
	odd=[]
	k=0
	for i in range(len(arr)): 
		if (arr[i]%2==1): odd.append(arr[i])
	odd.sort()
	for i in range(len(arr)):
		if arr[i]%2==1: 
			arr[i]=odd[k]
			k+=1
	return arr

print(sort_array([5,3,2,8,1,4]))

