from Graph import Graph
graph = {}
graph["start"] = {}
graph["start"]["a"] = 5
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["c"] = 4
graph["a"]["d"] = 2

graph["b"] = {}
graph["b"]["a"] = 8
graph["b"]["d"] = 7

graph["c"] = {}
graph["c"]["d"] = 6
graph["c"]["finish"] = 3

graph["d"] = {}
graph["d"]["finish"] = 1

graph["finish"] = {}

g = Graph(graph, "start", "finish")
parents = g.parents
costs = g.costs
infinity = g.infinity
'''infinity = float("inf")
costs = {}
costs["a"] = 5
costs["b"] = 2
costs["c"] = infinity
costs["d"] = infinity
costs["finish"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = None
parents["d"] = None
parents["finish"] = None'''


processed = []

def findLowestCostNode(costs):
	smallest = infinity
	key = None
	for k in costs.keys():
		if costs[k] < smallest and k not in processed:
			smallest = costs[k]
			key = k
	return key

def printPath(parents, finishNode):
	key = finishNode
	path = [finishNode]
	while parents[key] != "start":
		path.append(parents[key])
		key = parents[key]
	path.append(parents[key])
	path.reverse()
	return path

node = findLowestCostNode(costs)

while node is not None:
	cost = costs[node]
	neighbors = graph[node]
	for n in neighbors.keys():
		newCost = cost + neighbors[n]
		if costs[n] > newCost:
			costs[n] = newCost
			parents[n] = node
	processed.append(node)
	node = findLowestCostNode(costs)
print(parents)
print(costs)
print(printPath(parents, "finish"))