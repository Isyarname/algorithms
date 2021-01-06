from timeit import timeit
from random import shuffle

def findSmallest(unsortedList: list):
	smallest = unsortedList[0]
	smallestIndex = 0
	for i in range(1, len(unsortedList)):
		if unsortedList[i] < smallest:
			smallest = unsortedList[i]
			smallestIndex = i
	return smallestIndex

def selectionSort(unsortedList: list):
	'''
	O(n^2)
	'''
	sortedList = []
	for i in range(len(unsortedList)):
		smallest = findSmallest(unsortedList)
		sortedList.append(unsortedList.pop(smallest))
	return sortedList
l = list(range(0, 100000))
shuffle(l)
shuffledList = l
elapsedTime = timeit('selectionSort(shuffledList)', 'from __main__ import shuffledList, selectionSort, findSmallest', number=1)
print(elapsedTime)