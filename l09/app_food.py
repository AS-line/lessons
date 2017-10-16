import random
def my_cook(*args, major = 'мазик'):
	for product in args:
		# print('Пожарим ' + product)
		making_food(product)
	print('Обильно нальём ', major)

def making_food(ingridient):
	print(random.choice(cook_variants) + ' ' +
		ingridient)	

cook_variants = ['Пожарим', "Сварим", "Разгоним", "Похороним"]
name = ['яйца', "молоко", "процессор", "труп кошки",
	'кошачий корм']

my_cook('яйца', "молоко", "процессор", "труп кошки",
	'кошачий корм')
print(''.join([c[0] for c in name]))