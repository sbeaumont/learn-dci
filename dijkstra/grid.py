"""
dijkstra.py

Created by Serge Beaumont on 2011-12-10.

A Context and Role that know how to connect objects into a grid.
Note that in the Dijkstra example I 'export' the whole grid, roles
and all, to the Dijkstra context. I wonder if this is a valid scenario
of breaking strict role encapsulation. After all, I want node behavior
and state to persist to another Context.
"""

from dci import Context, Role

class Grid(Context):
	def __init__(self):
		self.nodes = dict()
		
	def addNode(self, name, obj):
		self.nodes[name] = Node(obj)
		
	def link(self, node1Name, node2Name, weight):
		node1 = self.nodes[node1Name]
		node2 = self.nodes[node2Name]
		node1.addNeighbour(node2, weight)
		node2.addNeighbour(node1, weight)

class Node(Role):
	def __init__(self, ob):
		self.neighbours = dict()
	
	def addNeighbour(self, node, weight):
		self.neighbours[node] = weight