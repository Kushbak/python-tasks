arrOfNums = []
howMany = int(input()) 
items = input()    
finded = 0
if len(items.split()) == howMany and howMany <= 1000:
	searchNum = input()
	arrOfNums = items.split()
	i = 0
	while i < len(arrOfNums): 
		if arrOfNums[i] == searchNum: 
			finded = i 
		i += 1  

	if arrOfNums[finded] == searchNum:
		print('YES')
	else:
		print('NO') 