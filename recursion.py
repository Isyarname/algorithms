def sum(l):
	if len(l) > 0:
		return l[0] + sum(l[1:])
	else:
		return 0

def lenght(l):
	if l == []:
		return 0
	else:
		return 1 + lenght(l[1:])

def factorial(n):
	if n == 1:
		return 1
	elif n > 1:
		return n * factorial(n-1)
	else:
		print("меньше 1 нельзя!!!111111111111111111111")

print(factorial(9))