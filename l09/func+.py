def my_func(name):
	print('Здрасти ' + name)

# my_func('Султанмурад')

def my_sum(a,b):
	# print(a + b)
	return a + b
ab_sum = my_sum(25, 50)

# number1 = int(input('1 :'))
# number2 = int(input('2 :'))
# print(my_sum(number1, number2))

# def my_divide(n, m, l, k, p, o):
# 	res = n / m + p * o + k / l 
# 	return res
# print(my_divide(n = 15, m = 5, o = 15, k = 20, p = 40, l = 18))

# def group(name1 = "Саид", name2 = "Султанмурад",name3 = "Руслан"):
# 	group_list = 'В нашей группе есть ' + name1 + name2 + name3
# 	return group_list

# print(group('Гаджи ', 'Аслан'))

# print(30, 29, sep=' разбить ')
# print(30, 29, sep= '\n')

def human_list(*args, **kwargs):
	for humans in args:
		print(humans, ' оглы')
	print(kwargs)
human_list('Адам', "Ева", 'Кайн', 'Авель', gotfather = 'Крёстный отец', hogfather = 'Санто')