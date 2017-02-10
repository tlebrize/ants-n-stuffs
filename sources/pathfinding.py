import collections

class Queue(object):
	def __init__(self):
		self.queue = collections.deque()

	def get(self):
		if len(self.queue):
			return self.queue.popleft()

	def put(self, elem):
		self.queue.append(elem)

	def empty(self):
		return len(self.queue) == 0


def reverse(board, nodes):
	current = None
	for n in nodes:
		if n.name == "Start":
			current = n

	if not current or not current.visited:
		return

	while current.name is not "End":
		board.lightNode(current)
		current = current.origin

def breadth_first_search(nodes):
	end = None
	for n in nodes:
		if n.name == "End":
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
			if neighbor.name == "Start":
				return
