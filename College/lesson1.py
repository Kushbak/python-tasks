#       1
print()
print('Задача 1')
num1 = int(input('Введите часы: '))
num2 = int(input('Введите минуты: '))
num3 = int(input('Введите секунды: '))

def checkTime(hour, minute, seconds):
	print(str(((hour * 60) + minute) * 60 + seconds) + ' секунд' )

checkTime(num1, num2, num3)


#       2
print()
print('Задача 2.1')
celsiaDegree = int(input('Введите температуру в цельсиях: '))

def toFar(t):
	print(str(9 / 5 * t + 32) + ' градусов фаренгейт')

toFar(celsiaDegree)
 

#       3
print()
print('Задача 2.2')
nums = input('Введите 9 чисел через запятую для вычисления a, b, c, d, e, f, g, k, p: ')
if len(nums.split(',')) == 9:
	arr = list(map(int, nums.split(',')))
	ex1 = (arr[0] + arr[1]) * arr[2] + arr[3] * (arr[4]/arr[5])
	ex2 = arr[7] + arr[8] * (arr[0]/arr[1]) + arr[6]
	print((ex1/ex2) * (4/5))
else: 
	print('Неправильный ввод данных')