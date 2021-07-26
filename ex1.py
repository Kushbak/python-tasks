# x = int(input())
# L = 0
# M = 0 
# 	while x > 0:
# 		M += 1
# 		if x%2 != 0:
# 			L = L + 1
# 		x = x // 2
# print(L)  
# print(M)   

# x = int(input())
# L = 0
# M = 0 
# while x > 0:
# 	M += 1
# 	if x%2 != 0:
# 		L = L + 1
# 	x = x // 2
# print(L)  
# print(M)   


# x должно умножаться 8 раз(в степени 8)
# оно должно быть четным 4 раза

def Func():
	x = 300
	while x > 0:
		a = x
		L = 0
		M = 0
		while a > 0:
			M += 1
			if a%2 != 0:
				L = L + 1
		a = a // 2
		x -= 1
		if L == 4 and M == 8:
			x = -1

		print(x, L, M) 

Func()