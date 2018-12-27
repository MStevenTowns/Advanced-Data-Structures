
'''
M. Steven Towns 
9/25/16
Homework 1
Part B-1
THIS MUST BE RUN WITH PYTHON 3
'''

def computeSpans1(P):
    S=[]
    for i in range(len(P)):
        k=0
        done=False
        while (k<=i and not done):
            if P[i-k]<=P[i]:
                k+=1
            else:
                done=True
            #    break
        S.append(k)
    return S
    
    
##input and formating, ignore for speed testing    
usrIn=input("Please give a list of stock prices separated by a space: ")
P=usrIn.strip().split(" ")
P=[float(i) for i in P]
##end of input and formating

print(computeSpans1(P))
