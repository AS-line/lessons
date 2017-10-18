import math
print("Введике коэффициенты ax^2 + bx + c = 0")
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
disk = b**2 - 4*a*c
if disk < 0:
	print('Нет корней')
elif disk == 0:
	x = -b/2*a
	print('Ур-е имеет один корень это: ', x)
elif disk > 0:
	x1 = -b + math.sqrt(disk) / 2*a
	x2 = -b - math.sqrt(disk) / 2*a
	print('Два  корня х1 = ', x1,'х2 = ', x2)