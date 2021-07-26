arrOfNums = []

num1 = int(input())
num2 = int(input())

if num1 < 100 and num2 < 100:
	if num1 > num2: 
		while num1 > num2: 
			if num2%5 == 2:
				arrOfNums.append(num2)
			elif num2%5 == 3:
				arrOfNums.append(num2) 

			num2 += 1
		
	else: 
		while num1 < num2:
			if num1%5 == 2:
				arrOfNums.append(num1)
			elif num1%5 == 3:
				arrOfNums.append(num1) 

			num1 += 1 

if len(arrOfNums) :
	for num in arrOfNums:
		print(num)
else:
	print('No any number')

print(arrOfNums)

 