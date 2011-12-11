"""
dijkstra.py

Created by Serge Beaumont on 2011-12-10.

Implementation of the Dijkstra algorithm. Does not need 'Manhattan form',
will work on any graph.

Yes, it works, but I'm not happy with one thing: role/context scope state.
This implementation works because it can depend on littering an object with
state which is then available for all time. I don't like this. Just like
Roles have context scope, I believe that there is state that should be able
to have context scope too...

Another question is that this Context has a dependency on the grid.Node role,
because I want walk over the grid. This makes sense, methinks, because
nodes need to remember the notion of neighbours to remain a grid. Still, it
is a violation of DCI encapsulation so this needs some looking into. To be honest
I have an issue with Data being global and that you need to preattach instance
variables just in case they're used by some role. That does not sit right with me:
I believe state should be just as dynamic as roles, although with a different
lifecycle.

Note how short the scope is of some Roles, just a single method call...
e.g.
dNode = Node(rootNode)
dNode.setBest(dNode, 0)

My big issue is: how do I cleanly deal with the bestNode and bestWeight state
that I do NOT want to have surviving beyond its proper scope?

"""
from dci import Context, Role
from collections import deque

class Dijkstra(Context):
	def __init__(self, grid):
		self.grid = grid

	def printShortestPathFor(self, start, destination):
		path = self.shortestPath(start, destination)
		pathString = ", ".join([node.name for node in path])		
		print "From", start, "to", destination, ":", pathString

	def shortestPath(self, fromName, toName):
		rootNode = self.grid.nodes[fromName]
		endNode = Node(self.grid.nodes[toName])

		# Initialize the root node to 0 weight
		dNode = Node(rootNode)
		dNode.setBest(dNode, 0)
		
		self.calculateWeights(rootNode)
		
		return self.backtrackShortestPath(endNode, dNode)

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
		while path[0] != rootNode:
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
		# The if is needed to prevent resetting state when I wrap
		# an object multiple times with this role.
		# Yes, it's icky and it needs some thinking over...
		if not hasattr(self, "bestNode"):
			self.bestNode = None
			self.bestWeight = float("inf")

	def setBest(self, node, weight):
		"Only accept a new best weight if it's better, i.e. lower than I have."
		if weight < self.bestWeight:
			self.bestNode = node
			self.bestWeight = weight

	def calculateTentativeWeight(self):
		"Calculate the weights of my neighbours"
		for node, weight in self.neighbours.iteritems():
			# Extremely short scope of role: only one method call :-)
			node = Node(node)
			node.setBest(self, self.bestWeight + weight)