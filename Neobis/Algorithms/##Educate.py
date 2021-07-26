# Нахождение числа в массиве, линейный поиск в несортированном списке
# j = -1
# i = 0
# n = 0
a = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10, 11, 0, 12, 13 , 14, 15]
# while i < len(a): 
# 	if a[i] == 5:
# 		j = i
# 		print(a[j])
# 	i += 1 



# Поиск минимума
# imin = 0
# i = 0 
# while i < len(a):
# 	if a[i] < a[imin]:
# 		imin = i
# 		print(a[i])
# 		print(imin)
# 	i += 1



# Поиск минимума и максимума 
imin = 0
imax = 0
i = 0 
while i < len(a):
	if a[i] < a[imin]:
		imin = i 
		print(a[imin])

	if a[i] > a[imax]:
		imax = i 
		print(a[imax])
	i += 1
