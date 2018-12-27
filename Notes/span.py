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

P=[4,3,1,2,1,3,7]
#print(computeSpans1(P))

from stackData import stackData
def computeSpans2(P):
    D=stackData()
    S=[]
    for i in range(len(P)):
        h=0
        done=False
        while not(D.isEmpty() or done):
            if P[i]>=P[D.peek()]:
                D.pop()
            else: 
                done=True
                #break

        if D.isEmpty():
            h=-1
        else:
            h=D.peek()
        S.append(i-h)
        D.push(i)
    return S
P=[4,3,1,2,1,3,7]
print(computeSpans2(P))
