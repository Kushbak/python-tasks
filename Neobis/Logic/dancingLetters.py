def callFunc():  
	one = 1
	while one: 
		someText = input()

		dancinText = ''
		digitForDance = 1 
		if len(someText) > 0:
			for letter in someText:
				if letter.isalpha():
					if int(digitForDance) % 2 == 0:
						digitForDance += 1
						dancinText += letter.lower()  
					
					elif int(digitForDance) % 2 == 1:
						digitForDance += 1
						dancinText += letter.upper()   
				else: 
					dancinText += letter 

			print(dancinText) 

callFunc() 
 