import Queue

def hotPotatoe(nameList, num):
	simQueue=Queue.Queue()
	for name in nameList:
		simQueue.enqueue(name)
	while simQueue.size()>1:
		for i in range(num):
			simQueue.enqueue(simQueue.dequeue())
		simQueue.dequeue()
	return simQueue.dequeue()
print(hotPotatoe(['bill', 'david'],7))
