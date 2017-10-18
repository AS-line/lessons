import random
def my_class(name):
	a = random.randint(1, 2)
	if a == 1:
		print(name + ' молодец')
	elif a == 2:
		print(name + ' не молодец')
my_class('Руслан')
