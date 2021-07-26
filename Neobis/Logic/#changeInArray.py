nums = []
num = 0

def callFunc():
	i1 = 0
	while 10 > i1:
		num = int(input())
		if -100000 < num < 100000:
			if num <= 0: 
				nums.append(1)
				print('N[' + str(i1) + '] = 1')
			else:
				nums.append(num)
				print('N[' + str(i1) + '] = ' + str(num))
			i1 += 1
 
callFunc()




# nums = []
# num = 0

# def callFunc():
# 	i1 = 0
# 	while 3 > i1:
# 		i1 += 1 
# 		global num
# 		num = input()
# 		nums.append(num)
# 	someFunc() 

# def someFunc():
# 	i2 = 0
# 	for num in nums:
# 		if int(num) < 0:
# 			nums.pop(i2).append(1) 
# 		else:
# 			for str(sym) in num:
# 				if sym == 0:
# 					nums.pop(i2).append(1)  

# 		print(num)
# 	print(nums)


# callFunc()
#  