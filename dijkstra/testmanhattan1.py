#!/usr/bin/env python
# encoding: utf-8
"""
testmanhattan1.py

Created by Serge Beaumont on 2011-12-10.
"""

from grid import Grid
from dijkstra import Dijkstra

class Intersection(object):
	def __init__(self, name):
		self.name = name

def createGrid():
	grid = Grid()
	
	# Populate the grid with nodes
	grid.addNode('a', Intersection('a'))
	grid.addNode('b', Intersection('b'))
	grid.addNode('c', Intersection('c'))
	grid.addNode('d', Intersection('d'))
	grid.addNode('e', Intersection('e'))
	grid.addNode('f', Intersection('f'))
	grid.addNode('g', Intersection('g'))
	grid.addNode('h', Intersection('h'))
	grid.addNode('i', Intersection('i'))
	
	# Grid is of Manhattan form:
	#
	#    a - 2 - b - 3 - c 
	#    |       |       |
	#    1       2       1
	#    |       |       |
	#    d - 1 - e - 1 - f
	#    |               |
	#    2               4
	#    |               |
	#    g - 1 - h - 2 - i
	#
	#    11 links
	#
	# Link all the nodes according to schema above
	
	grid.link('a', 'b', 2)
	grid.link('a', 'd', 1)
	grid.link('b', 'c', 3)
	grid.link('b', 'e', 2)
	grid.link('c', 'f', 1)
	grid.link('d', 'e', 1)
	grid.link('d', 'g', 2)
	grid.link('e', 'f', 1)
	grid.link('f', 'i', 4)
	grid.link('g', 'h', 1)
	grid.link('h', 'i', 2)
	
	return grid

def main():
	grid = createGrid()
	dijkstraGrid = Dijkstra(grid)
	path = dijkstraGrid.shortestPath('a', 'i')
	pathString = ''
	for node in path:
		pathString += node.name + ", "
	print pathString
	

if __name__ == '__main__':
	main()

