from timeit import timeit
from random import shuffle

def quickSort(unsortedList):
	if len(unsortedList) < 2:
		return unsortedList
	else:
		pivot = unsortedList[len(unsortedList)//2]
		less = [i for i in unsortedList[1:] if i <= pivot]
		greater = [i for i in unsortedList[1:] if i > pivot]
		return quickSort(less) + [pivot] + quickSort(greater)

l = list(range(0, 1000000))
shuffle(l)
shuffledList = l
elapsedTime = timeit('quickSort(shuffledList)', 'from __main__ import shuffledList, quickSort', number=1)
print(elapsedTime)