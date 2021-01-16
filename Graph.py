class Graph:
	def __init__(self, graph: dict, startNode, finishNode):
		self.start = startNode
		self.finish = finishNode
		self.graph = graph
		self.costs = {}
		self.parents = {}
		self.infinity = float("inf")
		self.fill()

	def fill(self):
		for k in self.graph.keys():
			self.parents[k] = None
			self.costs[k] = self.infinity
		for n in self.graph[self.start].keys():
			print("n:", n)
			print(self.start)
			print(self.graph[self.start][n])
			self.parents[n] = self.start
			self.costs[n] = self.graph[self.start][n]
