def BinarySearch01(A,k):
	low=0
	high=len(A)-1
	while True:
		mid=(low+high)//2
		#print(A[mid])
		if A[mid]==k:
			return mid
		elif A[mid]>k:
			high=mid-1
		else: 
			low=mid+1
		if low>=high:
			return "NIL"

def BinarySearch02(A, k, low, high):
	if(low>high):
		return "NIL"
	else:
		mid=(low+high)//2
		#print(A[mid])
		if k==A[mid]:
			return mid
		elif k<A[mid]:
			return BinarySearch02(A, k, low, mid-1)
		else:
			return BinarySearch02(A, k, mid+1, high)
A=[i for i in range(100)]
print(A)
print(BinarySearch01(A, k))
print(BinarySearch02(A, k, 0, len(A)))
