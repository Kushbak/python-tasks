print('Задача 1')

def first():
	num1 = int(input('Введите первое число: '))
	num2 = int(input('Введите второе число: '))

	if num1 <= num2:
		while num1 <= num2:
			print(str(num1) + '^2: ' + str(num1**2))
			num1 += 1
	else:
		while num1 >= num2:
			print(str(num2) + '^2: ' + str(num2**2))
			num2 += 1
first()

print('')
print('Задача 2')

def second():
	num = input('Введите натуральное число: ')

	summ = 0
	for a in num:
		summ += int(a)

	print('Сумма цифр в введеннем числе:' + str(summ))

second() 