print()
print('Задача 1')

def task1():
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

task1()



print()
print('Задача 2')

def task2():
	arr = [177, 172, 175, 165, 200, 188, 182, 173, 150, 187, 188, 158]

	print('Самый высокий: ' + str(max(arr)))
	print('Самый низкий: ' + str(min(arr)))

task2()



print()
print('Задача 3')

def task3():
	words = input('Введите несколько слов через пробел: ')
	arr = list(map(str, words.split()))

	shortest = ''
	shortestLength = 999 
	for word in arr:
		if shortestLength > len(word): 
			shortestLength = len(word)
			shortest = word

 
	print('Самое короткое слово: ' + shortest + '. Число символов: ' + str(shortestLength))

task3()



print()
print('Задача 4')

def task4():
	print()
	num1 = input('Введите 1е число: ')
	num2 = input('Введите 2е число: ')

	if(num1.isdigit() and num2.isdigit()):
		print(int(num1) + int(num2))
	else:
		print('Введите число!!!')
		task4()

task4() 



print()
print('Задача 5')
print()

def task5():
	correctLogin = 'login'
	correctPass = 'login123'

	def setInput(): 
		newLogin = input('Введите логин(login): ')
		newPass = input('Введите пароль(login123): ')
		if len(newPass) > 0: 
			check(newLogin, newPass)

	def check(newLog, newPass):
		if newPass == correctPass and newLog == correctLogin:
			print('Добро пожаловать ' + correctLogin + '!') 
		else:
			print('Неправильный логин или пароль!')  
			setInput() 

	setInput()
	
task5()