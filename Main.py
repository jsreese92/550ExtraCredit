'''
Created on Apr 30, 2014

@author: jsreese
'''

from Vertex import Vertex
from Edge import Edge
from A_star import A_star

def readFile():
  """ returns tuple containing (numVertices, numEdges, vertexList, edgeList,
  sourceVertex, destVertex)"""
  #f = open('map_input.txt','r')
  f = open('usa.txt','r')
  vertexList = []
  edgeList = []
  
  newlineCount = 0
  for line in f:

    if (line.isspace()): #newline
      newlineCount += 1
      #print "count incremented to: %s" % newlineCount
      continue # starts next loop iteration
      
    if (newlineCount == 1):
      split = line.split()
      numVertices = split[0]
      numEdges = split[1]
      #print "numVertices: %s, numEdges: %s" % (numVertices, numEdges)
    if (newlineCount == 2):
      tempList = []
      split = line.split()
      v = Vertex(int(split[0]),int(split[1]),int(split[2]),999999,999999,tempList)
      vertexList.append(v)
      #print v.toString()
    if (newlineCount == 3):
      split = line.split()
      e = Edge(int(split[0]),int(split[1]))
      '''
      # put actual vertices in edge, not just index
      for v in vertexList:
        if (v.index == e.v0index):
          e.v0 = v
        if (v.index == e.v1index):
          e.v1 = v
      e.v0.neighborList.append(e.v1)
      e.v1.neighborList.append(e.v0)
      '''

      edgeList.append(e)
      #print e.toString()
    if (newlineCount == 4):
      split = line.split()
      sourceVertex = split[0]
      destVertex = split[1]
      #print "source: %s, destination: %s" % (sourceVertex, destVertex)
      
  return (numVertices,numEdges,vertexList,edgeList,sourceVertex,destVertex)
      
def initNeighbors(vertexList, edgeList):
  #sort vertexList
  sortedList = sorted(vertexList, key=lambda v:v.index)
  for e in edgeList:
    sortedList[e.v0index].neighborList.append(sortedList[e.v1index])
    sortedList[e.v1index].neighborList.append(sortedList[e.v0index])
  return sortedList
  #for v in sortedList:
  #  print v.index
  
  '''
      # put actual vertices in edge, not just index
      for v in vertexList:
        if (v.index == e.v0index):
          e.v0 = v
        if (v.index == e.v1index):
          e.v1 = v
      e.v0.neighborList.append(e.v1)
      e.v1.neighborList.append(e.v0)
      '''    
    

def main():
  # read in from text file
  fromFile = readFile()
  print "file loaded"
  numVertices = fromFile[0]
  numEdges = fromFile[1]
  vertexList = fromFile[2]
  edgeList = fromFile[3]
  sourceVertexIndex = int(fromFile[4])
  destVertexIndex = int(fromFile[5]) 
  
  print "initializing neighbors"
  sortedVertices = initNeighbors(vertexList,edgeList)
  sourceVertex = sortedVertices[sourceVertexIndex]
  destVertex = sortedVertices[destVertexIndex]
   
  #for v in vertexList:
  #  print "v (%s)'s neighbors: " % v.index
  #  v.printNeighbors()
    #if (v.index == sourceVertexIndex):
    #  sourceVertex = v
    #if (v.index == destVertexIndex):
    #  destVertex = v
    
  
  a = A_star() 
  print "finding shortest path"
  a.algorithm(sourceVertex,destVertex,vertexList)

main()