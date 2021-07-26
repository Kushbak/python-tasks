
def callFunc():
	employee = input()
	salary = input()
	sells = input()
	if salary and sells and employee:
		if 1000000 > float(salary) >= 0 and 1000000 > float(sells) >= 0 and len(employee) >= 1:
			percentOfSells = 15 * float(sells) / 100
			total = float(salary) + float(percentOfSells)
			print('TOTAL = R$ ' + str('{:.2f}'.format(total)))  

callFunc()

