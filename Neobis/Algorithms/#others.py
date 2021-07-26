arrOfNums = []
howMany = int(input()) 
items = input()    
finded = []
if len(items.split()) == howMany and 1 <= howMany <= 100000: 
	arrOfNums = items.split()

	for num in arrOfNums:
		if num not in finded:
			finded.append(num)
			 
	print(len(finded))