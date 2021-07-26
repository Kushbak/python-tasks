numIn = 0
numOut = 0

def callFunc(n):
	i = 0
	while howMany > i:
		i += 1
		nums = int(input())
		findNums(nums)
	print(str(numIn) + ' in')
	print(str(numOut) + ' out')

def findNums(n):
	if 20 >= n >= 10:
		global numIn
		numIn += 1
	else:
		global numOut
		numOut += 1 


howMany = int(input())
callFunc(howMany)