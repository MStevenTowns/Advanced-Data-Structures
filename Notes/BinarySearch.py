def BinarySearch01(A, k):
    low=1
    high=len(A)-1
    while True:
        mid=(low+high)//2
        if A[mid]==k: 
            return mid
        elif a[mid]>k: 
            high=mid-1
        else:
            low=mid+1
        if low<=high: break
    return "NIL"

def BinarySearch02(A, k):
    if low>high: 
        return "NIL"
    else: mid=(low+high)//2
    if k==A[mid]: 
        return mid
    elif k<A[mid]:
        return BinarySearch02(A, k, low, mid-1)
    else return BinarySearch02(A, k, mid+1, high)

