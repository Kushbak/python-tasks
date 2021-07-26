def callFunc(money):
	money = money
	banknote100 = 0
	banknote50 = 0
	banknote20 = 0
	banknote10 = 0
	banknote5 = 0
	banknote2 = 0

	coin100 = 0
	coin050 = 0
	coin025 = 0
	coin010 = 0
	coin005 = 0
	coin001 = 0

	i = 0.009
	while money > i: 

		if round(money, 2) >= round(100, 2):
			banknote100 += 1
			money -= 100	

		elif round(money, 2) >= round(50, 2):
			banknote50 += 1
			money -= 50

		elif round(money, 2) >= round(20, 2):
			banknote20 += 1
			money -= 20

		elif round(money, 2) >= round(10, 2):
			banknote10 += 1
			money -= 10

		elif round(money, 2) >= round(5, 2):
			banknote5 += 1
			money -= 5

		elif round(money, 2) >= round(2, 2):
			banknote2 += 1
			money -= 2


		elif round(money, 2) >= round(1, 2):
			coin100 += 1
			money -= 1

		elif round(money, 2) >= round(.50, 2):
			coin050 += 1
			money -= 0.50

		elif round(money, 2) >= round(.25, 2):
			coin025 += 1
			money -= 0.25

		elif round(money, 2) >= round(.10, 2):
			coin010 += 1
			money -= 0.10

		elif round(money, 2) >= round(.05, 2):
			coin005 += 1
			money -= 0.05

		elif round(money, 2) >= round(.01, 2):
			coin001 += 1
			money -= 0.01

	print('Banknotes:')
	print(str(banknote100) + ' Banknotes of 100 dollars')
	print(str(banknote50) + ' Banknotes of 50 dollars')
	print(str(banknote20) + ' Banknotes of 20 dollars')
	print(str(banknote10) + ' Banknotes of 10 dollars')
	print(str(banknote5) + ' Banknotes of 5 dollars')
	print(str(banknote2) + ' Banknotes of 2 dollars')
	print('Coins:')
	print(str(coin100) + ' Coins of 1.00 dollars')
	print(str(coin050) + ' Coins of 0.50 dollars')
	print(str(coin025) + ' Coins of 0.25 dollars')
	print(str(coin010) + ' Coins of 0.10 dollars')
	print(str(coin005) + ' Coins of 0.05 dollars')
	print(str(coin001) + ' Coins of 0.01 dollars')


money = round(float(input()), 2)

if money >= 0:
	callFunc(money)