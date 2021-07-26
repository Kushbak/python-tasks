# arrOfNums = []
# howMany = int(input()) 
# items = input()    
# finded = 0
# if len(items.split()) == howMany and howMany <= 1000:
# 	searchNum = input()
# 	arrOfNums = items.split()
# 	i = 0
# 	while i < len(arrOfNums): 

 
howMany = int(input()) 
items = list(map(int, input().split()))
searchNum = int(input())
def nearest(arr, num):
	print(min(items, key = lambda x: abs(x - num)))

nearest(items, searchNum)
