arrOfNums = []
howMany = int(input()) 
items = input()    
finded = ''
if len(items.split()) == howMany and howMany <= 1000:
	arrOfNums = list(map(int, items.split()))
	arrOfNums[arrOfNums.index(max(arrOfNums))], arrOfNums[0] = arrOfNums[0], max(arrOfNums)
	for num in arrOfNums:
		finded += str(num) + ' '
	print(finded)

# finded = ''
# howMany = int(input()) 
# if len(items.split()) == howMany and howMany <= 1000:
# 	arrOfNums = list(map(int, input().split()))
# 	arrOfNums.insert(arrOfNums.index(max(arrOfNums)), arrOfNums.pop(0))
# 	arrOfNums.insert(0, arrOfNums.pop(arrOfNums.index(max(arrOfNums))))
# 	for num in arrOfNums:
# 		finded += str(num) + ' '
# 	print(finded)
