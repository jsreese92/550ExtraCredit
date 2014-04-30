'''
Created on Apr 30, 2014

@author: jsreese
'''

from Vertex import Vertex

class Edge:
  v0index = 0
  v1index = 0
  v0 = Vertex(0,0,0,0,0,None)
  v1 = Vertex(0,0,0,0,0,None)
  
  def __init__(self,v0,v1):
    self.v0index = v0
    self.v1index = v1
    
  def toString(self):
    """Returns the string containing all an object's parameters"""
    return 'v0: %s, v1: %s.' % \
      (self.v0.toString(), self.v1.toString())
  
  def shortToString(self):
    return 'v0: %s, v1: %s' % (self.v0index, self.v1index)