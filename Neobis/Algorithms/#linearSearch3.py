arrOfNums = []
howMany = int(input()) 
items = input()    
finded = ''
if len(items.split()) == howMany and howMany <= 1000:
	searchNum = input()
	arrOfNums = items.split()
	i = 0
	while i < len(arrOfNums): 
		if arrOfNums[i] == searchNum: 
			finded += str(i + 1) + ' '
		i += 1   
	print(finded)