# 17 тема 

import random 
n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))
a = [[random.randint(10, 40) for i in range(m)] for j in range(n)]

averageOfColumn = []
average = 0

for i in range(len(a)):
	avg = 0
	for j in range(len(a[i])):
		avg += a[i][j]
		average += a[i][j]
		print('{:4d}'.format(a[i][j]), end = '')
	print()
	averageOfColumn.append(avg / len(a[i]))


average = average / (n*m)
print()
print('Среднее арифметическое данной матрицы: ' + str(round(average, 2)))
print('Наибольшее из средних значений каждой строки матрицы: ' + str(round(max(averageOfColumn), 2)))
