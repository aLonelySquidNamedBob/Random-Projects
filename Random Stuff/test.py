import math

num = 1000000
list1 = []
list2 = []

for i in range(num):
	x = i * 2 / 16 + 120
	list1.append(x)

for i in range(num):
	y = math.sqrt(list1[i])
	list2.append(y)

for i in range (num):
	print(list2[i])
