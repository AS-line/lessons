import sqlite3


def registration():
	descriptor = sqlite3.connect('DATA.db')
	runner = descriptor.cursor()

	idmeter = open("fileid", "r")
	usid = idmeter.read()
	usid += '1'
	idmeter.close()
	idmeter = open('fileid', 'w')
	idmeter.write(str(usid))
	idmeter.close()

	query = "INSERT INTO profiles_data VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
	date = usid, input('name:'), input('sername: '), input('language: '), input('age: '), input('country: '), input("login: "), input("passworld: ")
	runner.execute(query, date)

	descriptor.commit()
	runner.close()
	descriptor.close()
	print("YOU HAVE SUCCESSFULLY REGISTERED")

def log_in():
	descriptor = sqlite3.connect('DATA.db')
	runner = descriptor.cursor()

	runner.execute("SELECT login, password FROM profiles_data")
	profiles = runner.fetchall()
	true_login = input('login: ')
	check_profile = (true_login, input('passworld: '))
	if check_profile in profiles:
		print('YOU HAVE SUCCESSFULLY LOGGED')
		input("GO TO MENU")
		actions(true_login)
	else:
		print('INCORRECT USERNAME OR PASSWORD')
		выбор = input('TRY AGAIN?\n1)Y\n2)N\n')
		if выбор == '1':
			log_in()

	descriptor.commit()
	runner.close()
	descriptor.close()
	# return true_login

def actions(true_login):
	print("MENU")
	выбор = input('1)SHOW MY PROFILE\n2)EXIT\n')
	if выбор == '1':
		show_profile(true_login)

def show_profile(true_login):
	descriptor = sqlite3.connect('DATA.db')
	runner = descriptor.cursor()

	runner.execute("SELECT name, sername, language, age, country FROM profiles_data WHERE login = ?", [true_login])
	profile_data = runner.fetchall()
	print('Имя:' + profile_data[0][0])
	print('Фамилия:' + profile_data[0][1])
	print('Язык:' + profile_data[0][2])
	print('Возраст:' + str(profile_data[0][3]))
	print('Страна:' + profile_data[0][4])

	descriptor.commit()
	runner.close()
	descriptor.close()




def start():
	выбор = input('1)REG\n2)LOGIN\n')
	if выбор == '1':
		registration()
	elif выбор == '2':
		log_in()





true_login = start()