

def binary_search(A, x):
	nil = -1
	start = 0
	end = len(A)
	
	while start < end:
		mid = (start+end)/2
		if A[mid] == x:
			return mid
		elif A[mid] < x:
			start = mid + 1
		else:
			end = mid - 1
	
	if A[start]==x:
		return start
	else:
		return nil	


A = [3,1,2,8]
x = 3

print(len(A))
print(binary_search(A,x))		