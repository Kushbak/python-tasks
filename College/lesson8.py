#16 тема 

from random import randint

n = 10
a = [randint(1,99) for i in range(n)]
arr1 = []
arr2 = []

for i in a:
	if i % 3 == 0:
		arr1.append(i)
	if i % 5 == 0:
		arr2.append(i)

for i in range(len(arr1) - 1):
	for j in range(len(arr1) - i - 1):
		if arr1[j] > arr1[j+1]:
			arr1[j], arr1[j+1] = arr1[j+1], arr1[j]


for i in range(len(arr2) - 1):
	for j in range(len(arr2) - i - 1):
		if arr2[j] < arr2[j+1]:
			arr2[j], arr2[j+1] = arr2[j+1], arr2[j]


print(a)
print('3: ' + str(arr1))
print('5: ' + str(arr2))
