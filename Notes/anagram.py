import time

def anagramSolution2(s1,s2):
    list1=list(s1)
    list2=list(s2)

    list1.sort()
    list2.sort()
    
    pos=0
    matches=True
    while pos < len(s1) and matches:
        if list1[pos]==list2[pos]:
            pos=pos+1
        else: 
            matches=False
    return matches
start=time.time()
print(anagramSolution2('abcde','edcba'))
end=time.time()
print end-start


