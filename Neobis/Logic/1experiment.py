
def callFunc(a):
	i = 0

	cats = 0
	rats = 0
	frogs = 0
	
	while int(a) > i:
		i += 1 
		
		getAnimal = input().split()
		digit = int(getAnimal[0])
		nameOfAnimal = str(getAnimal[1])

		if 1 <= digit <= 15: 
			if nameOfAnimal == 'C':
				cats += digit
			elif nameOfAnimal == 'R':
				rats += digit
			elif nameOfAnimal == 'F':
				frogs += digit

	total = int(cats) + int(rats) + int(frogs)
	percentOfC = int(cats) * 100 / int(total)
	percentOfR = int(rats) * 100 / int(total)
	percentOfF = int(frogs) * 100 / int(total)

	print('Total: ' + str(total) + ' animals')
	print('Cats: ' + str(cats))
	print('Rats: ' + str(rats))
	print('Frogs: ' + str(frogs))
	print('Percentage of cats: ' + str('{:.2f}'.format(percentOfC)) + ' %')
	print('Percentage of rats: ' + str('{:.2f}'.format(percentOfR)) + ' %' )
	print('Percentage of frogs: ' + str('{:.2f}'.format(percentOfF)) + ' %' )

howMany = int(input())
callFunc(howMany)