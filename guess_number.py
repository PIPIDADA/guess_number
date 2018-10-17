import random

start = input('請輸入開始值：')
end = input('請輸入結束值：')
start = int(start)
end =int(end)
x = random.randint(start, end)
k = 0

while True:
	y = input('請於',start,'及',end,'中猜一個數：')
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


