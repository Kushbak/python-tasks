print('Задача 1')

def task1():
	numOfMonth = int(input('Введите номер месяца: '))
	
	if(0 < numOfMonth <= 2 or numOfMonth == 12):
		print('Зима')
	elif(2 < numOfMonth <= 5):
		print('Весна')
	elif(5 < numOfMonth <= 8):
		print('Лето')
	elif(8 < numOfMonth <= 11):
		print('Осень')
	else:
		print('Неправильный номер месяца')

task1()



print()
print('Задача 2')

def task2():
	apples = 100
	kg5 = 0
	kg10 = 0
	kg15 = 0
	while apples != 0:
		if(apples > 0 and apples - 15 >= 0):
			apples -= 15
			kg15 += 1 
		if(apples > 0 and apples - 10 >= 0):
			apples -= 10
			kg10 += 1 
		if(apples > 0 and apples - 5 >= 0):
			apples -= 5
			kg5 += 1 
	print(str(kg5) + ' ящиков по 5 кг яблок')
	print(str(kg10) + ' ящиков по 10 кг яблок')
	print(str(kg15) + ' ящиков по 15 кг яблок')  

task2()



print()
print('Задача 3')

def task3(num1, num2, num3): 
	arr = [num1, num2, num3]
	arr.sort()

	print(arr)

task3(1, 2, 3) # 3 числа для сортировки по возрастанию



print()
print('Задача 4')

def task4(): 
	num1 = int(input('Введите 1е число: '))
	num2 = int(input('Введите 2е число: '))

	while num1 != 0 and num2 != 0:
	    if num1 > num2:
	        num1 %= num2
	    else:
	        num2 %= num1

	gcd = num1 + num2
	print(gcd)

task4()



print()
print('Задача 5')

def task5(num):
	if(num == 0):
		return 0
	elif(num > 0):
		return 1
	elif(num < 0):
		return -1


print(task5(-15)) # число для выявления знака числа



print()
print('Задача 6')

def task6():
	arr = [5, 2, 3, 4, 3, 4, 5, 5, 5 , 3, 2, 5, 2, 3, 4, 5]
	mark = int(input('Введите оценку по пятибальной шкале: '))
	i = 0
	if(0 < mark <= 5):
		while i < len(arr):
			if(arr[i] == mark):
				print('Номер ' + str(i + 1) + ': ' + str(arr[i]) + ' оценка')
			i += 1
	else:
		print('Неправильно введена оценка')

task6()



print()
print('Задача 7')

def task7():
	arr = [177, 172, 175, 165, 200, 188, 182, 173, 150, 187, 188, 158]

	print('Самый высокий: ' + str(max(arr)))
	print('Самый низкий: ' + str(min(arr)))

task7()




