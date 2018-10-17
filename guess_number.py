import random

x = random.randint(1, 100)
k = 0

while True:
	y = input('請於1~100中選擇一個數：')
	y = int(y)
	k = k + 1
	if x > y:
		print('比答案小!')
	elif x < y:
		print('比答案大!')
	else:
		print('終於猜對了')
		print('你猜了',k,'次喔！！')
		break


