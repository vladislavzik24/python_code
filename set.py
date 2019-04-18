x = int(input())

while x > 0:
	y = x
	
	while y > 0:
		print(y)
		y -= 1
	x -= 1
	if x == 5:
		break
else:
	print('Цикл выполнился успешно!')