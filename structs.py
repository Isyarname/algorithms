from collections import deque
from timeit import timeit

graph = {}
# стартовый узел
graph["я"] = ["яна", "аня", "влад"]
# первый уровень узлов
graph["яна"] = ["егор", "света"]
graph["аня"] = ["ира"]
graph["влад"] = ["петя", "коля", "жора"]
# второй уровеень узлов
graph["егор"] = []
graph["света"] = []
graph["ира"] = []
graph["петя"] = []
graph["коля"] = []
graph["жора"] = []

'''graph = {}

graph["s"] = ["a", "b"]

graph["a"] = ["f"]
graph["b"] = ["a", "c"]
graph["c"] = ["f"]
graph["f"] = []
testGraph = graph'''


def isDesiredNode(name: str):
	return name == "f"

def breadthFirstSearch(startNode):
	searchQueue = deque()
	searchQueue += graph[startNode]
	checkedNodes = []
	while searchQueue:
		node = searchQueue.popleft()
		if not node in checkedNodes:
			if isDesiredNode(node):
				return {"result": True, "node": node}
			else:
				searchQueue += graph[node]
				checkedNodes.append(node)
	return {"result": False, "node": None}


elapsedTime = timeit('breadthFirstSearch("я")["node"]', 'from __main__ import isDesiredNode, breadthFirstSearch', number=100)//100
print(elapsedTime)