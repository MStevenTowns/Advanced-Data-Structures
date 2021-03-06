from Vertex import Vertex

class Graph:
	def __init__(self):
		self.vertList={}
		self.numVertices=0
	def addVertex(self,key):
		self.nuVertices=self.numVertices+1
		newVertex=Vertex(key)
		self.vertList[key]=newVertex
		return newVertex
	def getVertex(self,n):
		if n in self.vertList:
			return self.vertList[n]
		else:
			return None
			
	def __contains__(self,n):
		return n in self.vertList
	def addEdge(self,f,t,cost=0):
		if f not in self.vertList:
			nv=self.addVertex(f)
		if t not in self.vertList:
			nv=self.addVertex(t)
		self.vertList[f].addNeighbor(self.vertList[t],cost)
	def __iter__(self):
		return iter(self.vertList.values())

g=Graph()
for i in range(6):
	g.addVertex(i)
g.vertList
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)

for v in g:
	for w in v.getConnections():
		print("(%s, %s)" %(v.getID(),w.getID()))
