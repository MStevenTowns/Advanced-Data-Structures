'''
M. Steven Towns 
10/5/16
Homework 02
Part A
THIS MUST BE RUN WITH PYTHON 3
'''

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
print("Index: "+str(BinarySearch01(A, k)))

