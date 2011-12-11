"""
dijkstra.py

Created by Serge Beaumont on 2011-12-10.

Yes, it works, but I'm not happy with one thing: role/context scope state.
This implementation works because it can depend on littering an object with
state which is then available for all time. I don't like this. Just like
Roles have context scope, I believe that there is state that should be able
to have context scope too...

Note how short the scope is of some Roles, just a single method call...
e.g.
dNode = Node(rootNode)
dNode.setBest(dNode, 0)

"""
from dci import Context, Role
from collections import deque

class Dijkstra(Context):
	def __init__(self, grid):
		self.grid = grid

	def shortestPath(self, fromName, toName):
		rootNode = self.grid.nodes[fromName]
		endNode = Node(self.grid.nodes[toName])

		# Initialize the root node to 0 weight
		dNode = Node(rootNode)
		dNode.setBest(dNode, 0)
		
		self.calculateWeights(rootNode)
		
		return self.backtrackShortestPath(self)

	def calculateWeights(self, rootNode):
		"Does breadth first traversal, but also does the calculation as it goes along."
		visited = set()
		to_crawl = deque([rootNode])
		while to_crawl:
			current = to_crawl.popleft()
			if current not in visited:
				
				# Here we hook into the breadth first traversal and do the calculation.
				dNode = Node(current)
				dNode.calculateTentativeWeight()
				
				visited.add(current)
				node_children = set(current.neighbours)
				to_crawl.extend(node_children - visited)
		return list(visited)

	def backtrackShortestPath(self, endNode, rootNode):
		"Walk from end node via best nodes to root node to get shortest path."
		path = deque([endNode])
		while path[0] != dNode:
			path.appendleft(path[0].bestNode)
		return path
		

class Node(Role):
	"""A role that depends on grid.Node, it knows how to calculate
	weights for the Dijkstra algorithm. This is another thing I'm wondering about.
	Is this a legal way to 'break' encapsulation of roles? After all, I need the node
	behavior here..."""
	
	def __init__(self, ob):
		# This is the one thing I'm still not happy with.
		# How to deal with role/context-scope state in DCI???
		if not hasattr(self, "bestNode"):
			self.bestNode = None
			self.bestWeight = float("inf")

	def setBest(self, node, weight):
		if weight < self.bestWeight:
			self.bestNode = node
			self.bestWeight = weight

	def calculateTentativeWeight(self):
		"Calculate my own weights"
		for node, weight in self.neighbours.iteritems():
			# Extremely short scope of role: only one method call :-)
			node = Node(node)
			node.setBest(self, self.bestWeight + weight)