def merge(l1,l2):
	slot1=0
	slot2=0
	out=[]
	while(slot1<len(l1) && slot2<len(l2)):
		if(l1[slot1]<l2[slot2]):
			out.append(l1[slot1])
			slot1++
		elif(l1[slot1]>l2[slot2]):
			out.append(l2[slot2])
			slot2++
			
