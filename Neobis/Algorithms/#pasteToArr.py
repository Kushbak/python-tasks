arrOfNums = []
howMany = int(input()) 
items = input()    
numToArr, place = map(int, input().split())
finded = ''
if len(items.split()) == howMany and howMany <= 1000:
	arrOfNums = list(map(int, items.split()))
	arrOfNums.insert(place - 1, numToArr)
	for num in arrOfNums:
		finded += str(num) + ' '
	print(finded)

