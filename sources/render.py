import tkinter as tk
from tkinter import font as tkfont
import random

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
		self.canva = tk.Canvas(self.parent, height=h, width=w)
		self.canva.pack(fill=tk.BOTH, expand=1)
		for node in self.nodes:
			self.drawEdges(node)
		for node in self.nodes:
			self.drawNode(node)

	def drawEdges(self, node):
		x = int(node.X * self.scale + (self.scale * 0.5))
		y = int(node.Y * self.scale + (self.scale * 0.5))
		w = int(self.scale / 16)
		for neighbor in node.neighbors:
			nx = neighbor.X * self.scale + (self.scale * 0.5)
			ny = neighbor.Y * self.scale + (self.scale * 0.5)
			self.canva.create_line(x, y, nx, ny, width=w, fill="#9ad1ff")

	def drawNode(self, node):
		x = int(node.X * self.scale + (self.scale * 0.5))
		y = int(node.Y * self.scale + (self.scale * 0.5))
		s = int(self.scale * 0.35)
		t = int(self.scale * 0.65)
		font = tkfont.Font(size=-int(self.scale * 0.12))

		if node.name == "start":
			node.canva = self.canva.create_rectangle(
				x-s, y-s, x+s, y+s, width=0, fill="#8dff00")
			self.canva.create_text(x, y, width=t,
				font=font, text="Start")

		elif node.name == "end":
			node.canva = self.canva.create_rectangle(
				x-s, y-s, x+s, y+s, width=0, fill="#ff000e")
			self.canva.create_text(x, y, width=t,
				font=font, text="End")

		else:
			node.canva = self.canva.create_rectangle(
				x-s, y-s, x+s, y+s, width=0, fill="#008dff")
			self.canva.create_text(x, y, width=t,
				font=font, text=node.name)

	def lightNode(self, node):
		self.canva.itemconfig(node.canva, fill="#ff7200")

def render(nodes, X, Y, scale):
	root = tk.Tk()
	board = Board(root, nodes, X, Y, scale)
	board.lightNode(random.choice(list(nodes)))
	root.mainloop()

