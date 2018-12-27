class Vertex:
	def __init__(self,key):
		self.ID=key
		self.connectedTo={}
	def addNeighbor(self,vertex,weight=0):
		self.connectedTo[vertex]=weight
	def __str__(self):
		return str(self.ID)+' connectedTo: ' + str([x.ID for x in self.connectedTo])
	def getConnections(self):
		return self.connectedTo.keys()
	def getID(self):
		return self.ID
	def getWeight(self, vertex):
		self.connectedTo[vertex]

