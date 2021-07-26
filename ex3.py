def F(n):
	print(n, end='')
	if n >= 4:
		F(n - 1)
		F(n - 2)
		F(n - 2)

F(5)