#binary to dec.py
# Testing: [0, 0, 0, 1] ==> 1
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 0, 1] ==> 5
# Testing: [1, 0, 0, 1] ==> 9
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 1, 0] ==> 6
# Testing: [1, 1, 1, 1] ==> 15
# Testing: [1, 0, 1, 1] ==> 11
def binary_array_to_number(arr):
	res = 0
	pwd = len(arr)-1
	for x in range(0,len(arr)): 
		res += arr[x] * 2**pwd
		pwd -=1
	return res

print (binary_array_to_number([0,1,0,1]))
