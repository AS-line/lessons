class Users():
	def __init__(self, login, password):
		self.login = login
		self.password = password
	def register(self, users_list):
		users_list[self.login] = self.password
		if self.login in users_list:
			print('Такой пользователь уже существует')
			self.authorizate(users_list)
	def authorizate(self, users_list):
		if self.login in users_list:
			print('Успешная авторизация')
		else:
			print('Такого пользователя не существует')
			choice = input('1)Попробовать ещё 2)Зарегистрироваться')
			if choice == '1':
				self.authorizate(users_list)
			elif choice == '2':
				self.register(users_list)

def work(users_list):
	exit = 0
	enter = input('1)Войти 2)Зарегистрироваться 3)Выход')
	if enter == '1':
		user = Users(input('Введите логин'), input('Введите пороль'))
		user.authorizate(users_list)
	elif enter == '2':
		user = Users(input('Придумайте логин'), input('Придумайте пороль'))
		user.register(users_list)
	elif enter == '3':
		exit = 1
	return exit
users_list = {}
print('Добро пожаловать')
while True:
	exit = work(users_list)
	if exit == 1:
		break
	#work(users_list)
	# print(users_list)