#!/usr/env python

## ----------------------------------------------------------------------------
## SETUP

from random_words import RandomWords
import random

class Node(object):

	def __init__(self, x, y, neighbors, name):
		self.X = x
		self.Y = y
		self.neighbors = neighbors
		self.name = name
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
	for y in range(0, Y):
		for x in range(0, X):
			node_positions.append([x, y])

	# removes 'holes' nodes randomly
	to_remove = random.sample(node_positions, holes)
	for n in to_remove:
		node_positions.remove(n)

	# generate a list of random words to name each node
	rw = RandomWords()
	node_names = rw.random_words(count=len(node_positions))
	
	nodes = []
	for n in node_positions:
		nodes.append(Node(n[0], n[1], neighbors(n, node_positions),
			node_names.pop()))

	if len(nodes) >= 2:
		quart = len(nodes)/4
		random.choice(nodes[:quart]).flag = "start"
		random.choice(nodes[-quart:]).flag = "end"
	return nodes

## ----------------------------------------------------------------------------
## RENDER

import Tkinter as tk
import tkFont

class Board(tk.Frame):

	def __init__(self, parent, nodes, X, Y, scale):
		tk.Frame.__init__(self, parent)
		self.parent = parent
		self.nodes = nodes
		self.X = X
		self.Y = Y
		self.scale = scale * 80
		self.centerWindow()
		self.drawBoard()

	def centerWindow(self):
		w = self.X * self.scale
		h = self.Y * self.scale
		sw = self.parent.winfo_screenwidth()
		sh = self.parent.winfo_screenheight()
		x = (sw - w)/2
		y = (sh - h)/2
		self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

	def drawBoard(self):
		h = self.X * self.scale
		w = self.Y * self.scale
		self.caneva = tk.Canvas(self.parent, height=h, width=w)
		self.caneva.pack(fill=tk.BOTH, expand=1)
		for node in self.nodes:
			self.drawEdges(node)
		for node in self.nodes:
			self.drawNode(node)

	def drawEdges(self, node):
		x = int(node.X * self.scale + (self.scale * 0.5))
		y = int(node.Y * self.scale + (self.scale * 0.5))
		w = int(self.scale / 16)
		for neighbor in node.neighbors:
			nx = neighbor[0] * self.scale + (self.scale * 0.5)
			ny = neighbor[1] * self.scale + (self.scale * 0.5)
			self.caneva.create_line(x, y, nx, ny, width=w, fill="#4286f4")

	def drawNode(self, node):
		x = int(node.X * self.scale + (self.scale * 0.5))
		y = int(node.Y * self.scale + (self.scale * 0.5))
		s = int(self.scale * 0.35)
		t = int(self.scale * 0.65)
		font = tkFont.Font(size=-int(self.scale * 0.12))
		if node.flag == "start":
			self.caneva.create_rectangle(x-s, y-s, x+s, y+s, width=0, fill="#fff200")
			self.caneva.create_text(x, y, width=t, font=font, text="Start")
		elif node.flag == "end":
			self.caneva.create_rectangle(x-s, y-s, x+s, y+s, width=0, fill="#ff0015")
			self.caneva.create_text(x, y, width=t, font=font, text="End")
		else:
			self.caneva.create_rectangle(x-s, y-s, x+s, y+s, width=0, fill="#0ad64b")
			self.caneva.create_text(x, y, width=t, font=font, text=node.name)

def render(nodes, X, Y, scale):
	root = tk.Tk()
	board = Board(root, nodes, X, Y, scale)
	root.mainloop()

## ----------------------------------------------------------------------------
## OUTPUT


## ----------------------------------------------------------------------------
## MAIN

def main():
	X = 8
	Y = 6
	holes = int((25 * (X * Y)) / 100.0)
	nodes = setup_nodes(X, Y, holes)
	scale = 2
	render(nodes, X, Y, scale)

main()