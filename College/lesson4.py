# Дико извиняюсь за транслит
print('Задача 1')
# Словарь рыбы
def firstTask():
	Fishes = {
		'River': 'Sudak, Bersch, Okun\', Ersch' ,
		'Lake': 'Omul\', Harius, Golomyanka, Sig, Osetr',
		'Sea': 'Mintay, Osetr, Piksha, Okun\', Kil\'ka'
	}
	for item in Fishes:
		print(item)

	for item in Fishes:
		print(Fishes[item])
		
firstTask()



print()
print('Задача 2')
# Записать значение у в результате выполнения программы
def secondTask():
	y = 5
	for i in range(2, 6):
		y = y + 4 * i
	print(y)
	# Ответ 61

secondTask()

print()
print('Задача 3')
# Дан брусок длиной 20м
def thirdTask():
	brusok = 20
	poltora = 0
	dva = 0
	while brusok >= 0:
		if(brusok >= 0 and brusok - 2 >= 0):
			brusok = brusok - 2
			dva += 1
		else: 
			break

		if(brusok >= 0 and brusok - 1.5 >= 0):
			brusok = brusok - 1.5
			poltora += 1
		else:
			break

	print('1.5: ' + str(poltora) + ' отрезков') # 5
	print('2: ' + str(dva) + ' отрезков') 	   # 6
	print(str(brusok) + ' остаток')  

thirdTask()

print()
print('Задача 4')
# Записать значения переменных в таблицу
def fourthTask():
	k = 4
	p = 1040
	m = 2
	range = 1
	while p != m*m:
		k += 1
		p -= 4
		m *= 2 
		print(str(range) + ' Шаг цикла')
		print('k = ' + str(k))
		print('p = ' + str(p))
		print('m = ' + str(m))
		print('m*m = ' + str(m*m))
		range += 1
	# print(k)

fourthTask()

print()
print('Задача 5')
# Мааайнкрааафт
def fifthTask(hour):
	time = hour * 60
	machines = 1
	mineral = 0
	for i in range(time):
		mpm = machines * 4
		mineral += mpm 
		if(mineral >= 100): 
			mineral -= 100
			machines += 1
	# print('Заданное время в минутах: ' + str(time))
	print('Машин: ' + str(machines))
	# print('Остаток минералов: ' + str(mineral))
	# print('Минералов в минуту: ' + str(mpm)) 


fifthTask(1) # можно передать другую цифру как в часах 