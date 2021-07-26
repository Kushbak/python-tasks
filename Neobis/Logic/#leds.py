
def callFunc(a):
	i = 0
	if 1 <= a <= 2000:
		while a > i:
			i += 1
			num = input()
			if 1 <= len(num) <= 10100:
				led = 0

				for n in str(num):
					if n == '1':
						led += 2
					elif n == '2':
						led += 5
					elif n == '3':
						led += 5
					elif n == '4':
						led += 4
					elif n == '5':
						led += 5
					elif n == '6':
						led += 6
					elif n == '7':
						led += 3
					elif n == '8':
						led += 7
					elif n == '9':
						led += 6
					else:
						led += 6

				print(str(led) + ' leds')


howMany = int(input())
callFunc(howMany)