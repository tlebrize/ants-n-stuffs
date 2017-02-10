class Queue(object):
	def __init__(self):
		self.queue = []

	def get(self, i=0):
		if len(self.queue):
			return self.queue.pop(i)

	def put(self, elem):
		self.queue.append(elem)

	def empty(self):
		return len(self.queue) == 0


def reverse(board, nodes):
	current = None
	for n in nodes:
		if n.name == "start":
			current = n

	if not current or not current.visited:
		return

	while current.name is not "end":
		board.lightNode(current)
		current = current.origin

def breadth_first_search(nodes):
	end = None
	for n in nodes:
		if n.name == "end":
			end = n

	if not end:
		return

	end.visited = True
	frontier = Queue()
	frontier.put(end)
	while not frontier.empty():
		current = frontier.get()
		for neighbor in current.neighbors:
			if not neighbor.visited:
				frontier.put(neighbor)
				neighbor.visited = True
				neighbor.origin = current
			if neighbor.name == "start":
				return
