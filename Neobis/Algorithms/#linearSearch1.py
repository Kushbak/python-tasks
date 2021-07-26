arrOfNums = []
howMany = int(input()) 
items = input()  
finded = 0
if len(items.split()) == howMany and howMany <= 1000:
	searchNum = int(input())
	arrOfNums = items.split()
	i = 0
	while i < len(arrOfNums): 
		if arrOfNums[i] == str(searchNum):
			finded += 1 
		i += 1 
	print(finded)