print('Задача 1')
nums = input('Введите числа через запятую: ')
 
arr = list(map(int, nums.split(',')))  

array_d = {}.fromkeys(arr, 0)
for a in arr:
    array_d[a] += 1
  
print(array_d) 

print()
print('Задача 1')
