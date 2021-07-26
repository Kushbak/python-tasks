hundred = []

def setDig(n):
	i = 0 
	while n > i:
		i += 1  
		anyNum = int(input(str(i) + ' число: '))
		hundred.append(anyNum)
	showArr()

def showArr():
	maxNum = max(hundred)
	indexOfMax = hundred.index(maxNum)
	print('Самое большое число: ' + str(maxNum))
	print('Его индекс: ' + str(indexOfMax + 1))

nums = int(input('Количество чисел, которые вы хотите ввести: '))
setDig(nums)
 