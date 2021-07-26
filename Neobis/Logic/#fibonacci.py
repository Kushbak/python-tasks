def callFib(num):
	i1 = 0

	while i1 < int(num) :
		n = input() 
		i1 += 1
		findFib(n)

def findFib(n):
	fib1 = fib2 = 1
	i2 = 0

	if int(n) == 0:
		print('Fib(' + n + ') = ' + str(0))
	else:
		while i2 < int(n) - 2:
		    fibSum = fib1 + fib2
		    fib1 = fib2
		    fib2 = fibSum
		    i2 += 1

		print('Fib(' + n + ') = ' + str(fib2))

howMany = input()
callFib(howMany)

 