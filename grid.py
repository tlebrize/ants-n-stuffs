#!/usr/env python
from __future__ import division, print_function
from sources.render import render
from sources.setup import setup_nodes

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
	X = 5
	Y = 5
	scale = 2
	number_of_ants = 5
	holes = 13
	nodes = setup_nodes(X, Y, int((holes * (X * Y)) / 100.0))
	output(number_of_ants, nodes)
	render(nodes, X, Y, scale)

main()