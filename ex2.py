A = [8, 4, 3, 0, 7, 2, 1, 5, 9, 6]
s = 0
for j in range(9):
	if A[j] > A[j+1]:
		s = s + 1
		t = A[j]
		A[j] = A[j + 1]
		A[j + 1] = t


print(s)