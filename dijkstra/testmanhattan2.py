#!/usr/bin/env python
# encoding: utf-8
"""
testmanhattan2.py

Created by Serge Beaumont on 2011-12-11.
Copyright (c) 2011 Xebia BV. All rights reserved.
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
	grid.addNode('j', Intersection('j'))
	grid.addNode('k', Intersection('k'))

	#    Grid is of Manhattan form:
	#
	#    a - 2 - b - 3 - c - 1 - j
	#    |       |       |       |
	#    1       2       1       |
	#    |       |       |       |
	#    d - 1 - e - 1 - f       1
	#    |               |       |
	#    2               4       |
	#    |               |       |
	#    g - 1 - h - 2 - i - 2 - k
	#
	#    14 links
	#
	# Link all the nodes according to schema above

	grid.link('a', 'b', 2)
	grid.link('a', 'd', 1)
	grid.link('b', 'c', 3)
	grid.link('b', 'e', 2)
	grid.link('c', 'f', 1)
	grid.link('c', 'j', 1)
	grid.link('d', 'e', 1)
	grid.link('d', 'g', 2)
	grid.link('e', 'f', 1)
	grid.link('f', 'i', 4)
	grid.link('g', 'h', 1)
	grid.link('h', 'i', 2)
	grid.link('i', 'k', 2)
	grid.link('j', 'k', 1)

	return grid

def main():
	# First create a grid with grid.py
	grid = createGrid()
	
	# Then pass the grid to be processed by the Dijkstra algorithm
	# Note that I break encapsulation of the grid.py context here.
	# Good or bad...?
	dijkstraGrid = Dijkstra(grid)
	
	dijkstraGrid.printShortestPathFor('a', 'k')

	# I need a fresh grid if I want to do it twice.
	# See what I mean about context scoped state?
	# The old grid should be clean of Dijkstra state...
	grid = createGrid()
	dijkstraGrid = Dijkstra(grid)
	dijkstraGrid.printShortestPathFor('h', 'b')
	

if __name__ == '__main__':
	main()

