import sqlite3

desriptor = sqlite3.connect('DATA.db')
runner = desriptor.cursor()

runner.execute("""CREATE TABLE profiles_data (
	id NUMBER,
	name VARCHAR(30),
	sername VARCHAR(50),
	language VARCHAR(20),
	age NUMBER,
	country VARCHAR,
	login VARCHAR(20) PRIMARY KEY,
	password VARCHAR(20)
	)""")

desriptor.commit()
runner.close()
desriptor.close()