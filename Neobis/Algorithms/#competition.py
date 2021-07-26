arrOfNums = []
howMany = int(input())

def addToArr():
	i = 0
	if 1 <= howMany <= 1000:
		while i < howMany:
			items = list(map(int, input().split()))
			if len(items) == 2:
				arrOfNums.append(items)
			i += 1
		printFromArr()  

def printFromArr():
	s = sorted(arrOfNums, key = lambda x: x[0])
	s.sort(key = lambda x: x[1], reverse = True) 
	for item in s:
		finded = '' 
		for num in item:
			finded += str(num) + ' '
		print(finded.rstrip()) 
		
addToArr() 