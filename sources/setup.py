from random_words import RandomWords
import random, collections

class Node(object):

	def __init__(self, x, y, name):
		self.X = x
		self.Y = y
		self.name = name
		self.neighbors = list()
		self.canva = None

	def __str__(self):
		return "{}({}, {})".format(self.name, self.X, self.Y)

def get_neighbors(main, nodes):
	directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
	result = []
	for direction in directions:
		neighbor = (main[0] + direction[0], main[1] + direction[1])
		if neighbor in nodes.keys():
			result.append(nodes[neighbor])
	return result

def setup_nodes(X, Y, holes):
	rw = RandomWords()
	node_names = rw.random_words(count=X*Y)

	nodes = collections.OrderedDict()
	for y in range(0, Y):
		for x in range(0, X):
			nodes[(x, y)] = Node(x, y, node_names.pop())

	to_remove = random.sample(nodes.keys(), holes)
	for trm in to_remove:
		nodes.pop(trm)

	for node in nodes.values():
		node.neighbors = get_neighbors((node.X, node.Y), nodes)

	# Randomly puts flags on a random node. Start in the first 25%
	# and end in the last 25%.
	if len(nodes.keys()) >= 2:
		quarter = int(len(nodes.keys())/4.0 ) or 1
		first_quarter = list(nodes.keys())[:quarter]
		last_quarter = list(nodes.keys())[-quarter:]
		start = random.choice(first_quarter)
		nodes[start].name = "start"
		end = random.choice(last_quarter)
		nodes[end].name = "end"

	return nodes.values()
