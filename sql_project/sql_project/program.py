import tkinter
import sqlite3

window = tkinter.Tk()
window.title('Авторизация')
window.geometry('800x420')


def log_in(user_login, user_password):

	descriptor = sqlite3.connect('DATA.db')
	runner = descriptor.cursor()

	runner.execute("SELECT login, password FROM profiles_data")
	profiles = runner.fetchall()
	check_profile = (user_login, user_password)
	if check_profile in profiles:
		txt_label = tkinter.Label(text='YOU HAVE SUCCESSFULLY LOGGED', width=34)
		txt_label.place(x=20, y=70)
	else:
		txt_label = tkinter.Label(text='INCORRECT USERNAME OR PASSWORD')
		txt_label.place(x=20, y=70)

	descriptor.commit()
	runner.close()
	descriptor.close()



def registration():
	window.quit()


	window = tkinter.Tk()
	window.title('Авторизация')
	window.geometry('800x420')


	descriptor = sqlite3.connect('DATA.db')
	runner = descriptor.cursor()

	idmeter = open("fileid", "r")
	usid = int(idmeter.read())
	usid += 1
	idmeter.close()
	idmeter = open('fileid', 'w')
	idmeter.write(str(usid))
	idmeter.close()

	query = "INSERT INTO profiles_data VALUES (?,?,?,?,?,?,?,?,?)"
	date = usid,input('Имя:'),input('Фамилия: '), input("Логин: "), input("Пароль: "),None,None,None,None
	runner.execute(query, date)

	descriptor.commit()
	runner.close()
	descriptor.close()
	print("Успешная регистрация")


def show_profile(true_login):
	descriptor = sqlite3.connect('DATA.db')
	runner = descriptor.cursor()

	runner.execute("SELECT name, sername FROM profiles_data WHERE login = ?", [true_login])
	profile_data = runner.fetchall()
	print('Имя:' + profile_data[0][0])
	print('Фамилия:' + profile_data[0][1])

	descriptor.commit()
	runner.close()
	descriptor.close()


def enter_data(true_login):
	descriptor = sqlite3.connect('DATA.db')
	runner = descriptor.cursor()

	query = 'UPDATE profiles_data SET hours_working=? points_for_creativy=? points_for_working=? points_for_work=? payment=? WHERE login=?'
	data = input('Часы работы: '), input('Баллы за кративность: '),input('Баллы за проэкт: '), true_login
	runner.execute(query, data)

	descriptor.commit()
	runner.close()
	descriptor.close()


label_login = tkinter.Label(window, text='Login:')
label_login.place(x=0, y=0)

entry_login = tkinter.Entry(window)
entry_login.place(x=0, y=20)

label_password = tkinter.Label(window, text='Password:')
label_password.place(x=140, y=0)

entry_password = tkinter.Entry(window)
entry_password.place(x=140, y=20)

btn_log_in = tkinter.Button(window, text='Log in', width=36, bg='red')
btn_log_in.bind('<Button-1>', lambda event: log_in(str(entry_login.get()), str(entry_password.get())))
btn_log_in.place(x=2, y=40)

btn_reg_in = tkinter.Button(window, text='Or registration', width=36, bg='red')
btn_reg_in.bind('<Button-1>', lambda evnt: registration())
btn_reg_in.place(x=2, y=65)


window.mainloop()