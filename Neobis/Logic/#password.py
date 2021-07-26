correctPass = 2016
newPass = 0

def setPass():
	global newPass 
	newPass = input()
	if len(newPass) > 0: 
		check()

def check():
	if correctPass == int(newPass):
		print("Access permitted") 
	else:
		print("Incorrect password")  
		setPass() 

setPass()