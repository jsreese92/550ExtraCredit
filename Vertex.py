'''
Created on Apr 30, 2014

@author: jsreese
'''
from math import sqrt

class Vertex:
  index = 0
  x = 0
  y = 0
  gScore = 0 # path from source to this vertex
  fScore = 0 # gScore + straight-line distance from this vertex to goal
  neighborList = []
  
  def __init__(self,theIndex,theX,theY,theG,theF,theList):
    self.index = theIndex
    self.x = theX
    self.y = theY
    self.gScore = theG
    self.fScore = theF
    self.neighborList = theList
    
  def toString(self):
    """Returns the string containing all an object's parameters"""
    
    return 'index: %s, x: %s, y: %s, gScore: %s, hScore: %s' % \
      (self.index,self.x, self.y, self.gScore,self.fScore)
    
  def equals(self,otherVertex):
    """Returns true if given vertex has same x and y as other vertex"""
    if(self.x == otherVertex.x and self.y == otherVertex.y):
      return True
    return False
  
  def distance(self,otherVertex):
    """ returns distance between this node and another node"""
    return sqrt((otherVertex.x - self.x)**2 + (otherVertex.y - self.y)**2)
  
  def printNeighbors(self):
    for n in self.neighborList:
      print n.index
    
  
  