#!/usr/env python
from __future__ import division, print_function
from sources.render import render
from sources.setup import setup_nodes
from sources.pathfinding import breadth_first_search, reverse

def output(number_of_ants, nodes):
	print(number_of_ants)
	for node in nodes:
		if node.name == "start":
			print("##start")
		elif node.name == "end":
			print("##end")
		print("%s %s %s" % (node.name, node.X, node.Y))

	print("")

	done = []
	for node in nodes:
		for neighbor in node.neighbors:
			if "{}-{}".format(node.name, neighbor.name) in done:
				pass
			elif "{}-{}".format(neighbor.name, node.name) in done:
				pass
			else:
				done.append("{}-{}".format(node.name, neighbor.name))
				print("{}-{}".format(node.name, neighbor.name))

def main():
	X = 10
	Y = 8
	scale = 1.5
	number_of_ants = 5
	holes = 33
	nodes = setup_nodes(X, Y, int((holes * (X * Y)) / 100.0))
	output(number_of_ants, nodes)
	breadth_first_search(nodes)
	board = render(nodes, X, Y, scale)
	reverse(board, nodes)
	board.parent.mainloop()

main()