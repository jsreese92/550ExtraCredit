'''
Created on Apr 30, 2014

@author: jsreese
'''

from Vertex import Vertex
from math import sqrt

def hScore(startVertex,goalVertex):
  return sqrt(((startVertex.x - goalVertex.x)**2) + ((startVertex.y - goalVertex.y)**2))

class A_star:
  
  def algorithm(self,startVertex,goalVertex,vertexList):
    closedSet = set() # nodes already evaluated
    openSet = set() # set of nodes to be evaluated, initially contains startNode
    cameFrom = dict() # empty map of navigated nodes
    
    # add all vertices into openSet
    for v in vertexList:
      openSet.add(v)
    
    startVertex.gScore = 0
    # estimated total cost 
    startVertex.fScore = startVertex.gScore + hScore(startVertex,goalVertex) 
    
    while openSet: # while openSet is not empty
      current = min(openSet, key=lambda v:v.fScore) # node with lowest fScore
      if (current.equals(goalVertex)):
        #print "reconstruct path called"
        #return self.reconstructPath(cameFrom,goalVertex)
        print "shortest path: %s" % goalVertex.gScore
      openSet.remove(current)
      closedSet.add(current)
      for n in current.neighborList:
        if (n in closedSet):
          continue # may not be the same funciton as on wikipedia
        tempG = current.gScore + current.distance(n)
        
        #print "n: %s" % n.toString()
        #print "tempG: %s" % tempG
        if ((n not in openSet) or (tempG < n.gScore)):
          cameFrom[n] = current
          n.gScore = tempG
          n.fScore = n.gScore + hScore(n,goalVertex)
          if (n not in openSet):
            openSet.add(n)
            
  # don't need since only care what shortest path is
  '''
  def reconstructPath(self,cameFrom,currentNode):
    print "currentNode: %s" + currentNode.toString()
    """ Returns length of path from currentNode to goal"""
    pathWeight = 0
    if (currentNode in cameFrom):
      pathWeight += self.reconstructPath(cameFrom,cameFrom[currentNode])
      print "pathWeight: %s" % pathWeight
      return (pathWeight + currentNode.gScore)
    else:
      return currentNode.gScore
      '''
    
    
