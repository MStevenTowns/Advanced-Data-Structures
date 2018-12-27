#
#  adjGraph
#
#  Created by Brad Miller on 2005-02-24.
#  Copyright (c) 2005 Brad Miller, David Ranum, Luther College. All rights reserved.
#

import sys
import os
import unittest
from Queue import Queue

class Graph:
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0
        
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex
    
    def getVertex(self,n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertices
    
    def addEdge(self,f,t,cost=0):
            if f not in self.vertices:
                nv = self.addVertex(f)
            if t not in self.vertices:
                nv = self.addVertex(t)
            self.vertices[f].addNeighbor(self.vertices[t],cost)
    
    def getVertices(self):
        return list(self.vertices.keys())
        
    def __iter__(self):
        return iter(self.vertices.values())
                
class Vertex:
    def __init__(self,num):
        self.id = num
        self.connectedTo = {}
        self.color = 'white'
        self.dist = sys.maxsize
        self.pred = None
        self.disc = 0
        self.fin = 0

    # def __lt__(self,o):
    #     return self.id < o.id
    
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
        
    def setColor(self,color):
        self.color = color
        
    def setDistance(self,d):
        self.dist = d

    def setPred(self,p):
        self.pred = p

    def setDiscovery(self,dtime):
        self.disc = dtime
        
    def setFinish(self,ftime):
        self.fin = ftime
        
    def getFinish(self):
        return self.fin
        
    def getDiscovery(self):
        return self.disc
        
    def getPred(self):
        return self.pred
        
    def getDistance(self):
        return self.dist
        
    def getColor(self):
        return self.color
    
    def getConnections(self):
        return self.connectedTo.keys()
        
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
                
    def __str__(self):
        return str(self.id) + ":color " + self.color + ":disc " + str(self.disc) + ":fin " + str(self.fin) + ":dist " + str(self.dist) + ":pred \n\t[" + str(self.pred)+ "]\n"
    
    def getId(self):
        return self.id
'''
class DFSGraph(Graph):
	def __init(self):
		super().init__()
		self.time=0
	def dfs(self):
		for aVertex in self:
			aVertex.setColor('white')
			aVertex.setPred(-1)
		for aVertex in self:
			if aVertex.getColor()=='white'
			...
'''
def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile,'r')
    # create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g

def bfs(g,start):
	start.setDistance(0)
	start.setPred(None)
	vertQueue=Queue()
	vertQueue.enqueue(start)
	while(vertQueue.size()>0):
		currentVert=vertQueue.dequeue()
		for nbr in currentVert.getConnections():
			if(nbr.getColor()=='white'):
				nbr.setColor('grey')
				nbr.setDistance(currentVert.getDistance()+1)
				nbr.setPred(currentVert)
				vertQueue.enqueue(nbr)
			currentVert.setColor('black')
			
def traverse(x):
	while(x.getPred()):
		print(x.getId())
		x=x.getPred()
	print(x.getId())
	
				
'''
g=buildGraph("wordFile.txt")
bfs(g,g.getVertex("FOOL"))

traverse(g.getVertex('SAGE'))
'''
def posToNodeID(row,col,bdSize):
	return (row*bdSize)+col

def legalCoord(x,bdSize):
	return (x>=0 and x<bdSize)

def genLegalMoves(x,y,bdSize):
	newMoves=[]
	moveOffsets=[(-1,-2),(-1,2),(1,-2),(1,2),(-2,-1),(-2,1),(2,-1),(2,1),]
	for i in moveOffsets:
		newX=x+i[0]
		newY=y+i[1]
		if legalCoord(newX,bdSize) and legalCoord(newY,bdSize):
			newMoves.append((newX,newY))
	return newMoves
	
def knightGraph(bdSize):
	ktGraph=Graph()
	for row in range(bdSize):
		for col in range(bdSize):
			nodeID=posToNodeID(row,col,bdSize)
			newPositions=genLegalMoves(row,col,bdSize)
			for e in newPositions:
				nid=posToNodeID(e[0],e[1],bdSize)
				ktGraph.addEdge(nodeID,nid)
	return ktGraph

def orderByAvail(n):
	resList=[]
	for v in n.getConnections():
		if v.getColor()=='white':
			c=0
			for w in v.getConnections():
				if w.getColor()=='white':
					c=c+1
			resList.append((c,v))
	resList.sort(key=lambda x: x[0])
	return[y[1] for y in resList]
	
def knightTour(n,path,u,limit):
	u.setColor('grey')
	path.append(u)
	if n<limit:
		nbrList=list(orderByAvail(u))#change here
		i=0
		done=False
		while i<len(nbrList) and not done:
			if nbrList[i].getColor()=='white':
				done=knightTour(n+1, path,nbrList[i],limit)
				i=i+1
		if not done:
			path.pop()
			u.setColor('white')
	else:
		done=True
	'''
	for i in path:
		print(i.getId)
	'''
	return done
'''
side=8
graph=knightGraph(side)
knightTour(0,[],graph.getVertex(0),side*side-1)
'''
