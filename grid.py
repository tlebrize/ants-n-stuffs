#!/usr/env python

## ----------------------------------------------------------------------------
## SETUP

import random

class Node(object):

	def __init__(self, x, y, neighbors):
		self.X = x
		self.Y = y
		self.neighbors = neighbors
		self.flag = None


def neighbors(node, node_positions):
	directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
	result = []
	for direction in directions:
		neighbor = [node[0] + direction[0], node[1] + direction[1]]
		if neighbor in node_positions:
			result.append(neighbor)
	return result

def setup_nodes(X, Y, holes):
	node_positions = []
	for x in range(0, X):
		for y in range(0, Y):
			node_positions.append([x, y])
	for _ in range(0, holes):
		node_positions.pop(random.randint(0, len(node_positions)-1))
	nodes = []
	for n in node_positions:
		nodes.append(Node(n[0], n[1], neighbors(n, node_positions)))
	if len(nodes) >= 2:
		nodes[random.randint(0, X)].flag = "start"
		random_node = nodes[random.randint(len(nodes)-(2*holes), len(nodes)-holes)]
		while random_node.flag == "start":
			random_node = nodes[random.randint(0, len(nodes))]
		random_node.flag = "end"
	return nodes

## ----------------------------------------------------------------------------
## RENDER

import Tkinter as tk

class Board(tk.Frame):

	def __init__(self, parent, nodes, X, Y):
		tk.Frame.__init__(self, parent)
		self.parent = parent
		self.nodes = nodes
		self.X = X
		self.Y = Y
		self.centerWindow()
		self.drawBoard()

	def centerWindow(self):
		w = self.X * 80
		h = self.Y * 80
		sw = self.parent.winfo_screenwidth()
		sh = self.parent.winfo_screenheight()
		x = (sw - w)/2
		y = (sh - h)/2
		self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

	def drawBoard(self):
		h = self.X * 80
		w = self.Y * 80
		self.caneva = tk.Canvas(self.parent, height=h, width=w)
		self.caneva.pack(fill=tk.BOTH, expand=1)
		for node in self.nodes:
			self.drawEdges(node)
		for node in self.nodes:
			self.drawNode(node)

	def drawEdges(self, node):
		x = node.X * 80 + 40
		y = node.Y * 80 + 40
		for neighbor in node.neighbors:
			nx = neighbor[0] * 80 + 40
			ny = neighbor[1] * 80 + 40
			self.caneva.create_line(x, y, nx, ny, width=5, fill="#4286f4")

	def drawNode(self, node):
		x = node.X * 80 + 40
		y = node.Y * 80 + 40
		if node.flag == "start":
			self.caneva.create_rectangle(x-30, y-30, x+30, y+30, width=0, fill="#fff200")
		elif node.flag == "end":
			self.caneva.create_rectangle(x-30, y-30, x+30, y+30, width=0, fill="#ff0015")
		else:
			self.caneva.create_rectangle(x-30, y-30, x+30, y+30, width=0, fill="#0ad64b")

def render(nodes, X, Y):
	root = tk.Tk()
	board = Board(root, nodes, X, Y)
	root.mainloop()

## ----------------------------------------------------------------------------
## MAIN

def main():
	X = 20
	Y = 14
	holes = int((30 * (X * Y)) / 100.0)
	nodes = setup_nodes(X, Y, holes)
	render(nodes, X, Y)

main()