'''
M. Steven Towns 
10/5/16
Homework 02
Part B
THIS MUST BE RUN WITH PYTHON 3
'''

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

usrIn=input("Please give a list of numbers separated by a space (Enter for 0-99): ")
usrIn=usrIn.strip()
if usrIn=='':
	A=[i for i in range(100)]
else:
	A=usrIn.strip().split(" ")
	A=[int(i) for i in A]
	
	
usrIn=input("Please give number to search the list for (Enter for 75): ")

k=usrIn.strip()
if k=='':
	k=75
else:
	k=int(k)
print("Index: "+str(BinarySearch02(A, k, 0, len(A))))
