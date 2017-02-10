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
		quart = int(len(nodes)/4.0)
		start = random.choice(nodes[:quart])
		start.flag = "start"
		start.name = "name"
		end = random.choice(nodes[-quart:])
		end.flag = "end"
		end.name = "end"
	return nodes

