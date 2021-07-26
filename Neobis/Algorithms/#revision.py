# arrOfNums = []
# howMany = int(input()) 
# items = input()    	
# finded = ''
# if len(items.split()) == howMany and 2 <= howMany <= 1000: 
# 	arrOfNums = list(map(int, items.split()))
# 	arrOfNums.sort()
# 	print(str(arrOfNums[0]) + ' ' + str(arrOfNums[1])) 
 

# with linear search


arrOfNums = []
howMany = int(input()) 
items = input()  

min1 = 0
min2 = 0
if len(items.split()) == howMany and 2 <= howMany <= 1000: 
	arrOfNums = list(map(int, items.split()))
	i = 0
	while i < len(arrOfNums):
		if arrOfNums[i] < arrOfNums[min1]:
			min1 = i
		elif arrOfNums[i] < arrOfNums[min2] != arrOfNums[min1]:
			min2 = i
		i += 1
	print(str(arrOfNums[min1]) + ' ' + str(arrOfNums[min2]))
