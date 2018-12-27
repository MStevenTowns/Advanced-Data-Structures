#pretty sure none of these are right
'''
X=[2,4,8,2,1]
A=[9,9,9,9,9]
n=5
for i in range(len(X)-1):
    a=0
    for j in range(i):
        print(j) 
        a=a+X[j]
        
    
    A[i]=a/(i+1)
print(A)

#avg of all numbers up to this element

s=0
for i in range n:
    s=s+X[i]
a[i]=s/i+1

'''
'''
def prefixAverages(X):
    A=[]
    for i in range(len(X)):
        a=0
        for j in range(i):
            a=a+X[j]
            print a
        A.append(a/(i+1))
    #print A
prefixAverages([2,4,8,2,1])
'''
import time
def sumShit(n):
    return(n*((n+1))/2)
start=time.time()
print sumShit(10000000000000000000000000000)
end=time.time()
print(end-start)
