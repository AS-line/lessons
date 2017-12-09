import sqlite3
def saveindb(name, sername):
	descriptor = sqlite3.connect('db_file.db')
	runner = descriptor.cursor()


	runner.execute('''CREATE TABLE IF NOT EXISTS my_data (
		name VARCHAR(30) PRIMARY KEY,
		sername VARCHAR(30)
		)''')
	runner.execute('''INSERT INTO my_data VALUES (?,?)''', (str(name), str(sername)))
	descriptor.commit()

	runner.execute("SELECT * FROM my_data")
	table = runner.fetchall()
	for i in table:
		print('---------------------',i[0])

	runner.close()
	descriptor.close()