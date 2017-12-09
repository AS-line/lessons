import sqlite3

descriptor = sqlite3.connect('db_file.db')
runner = descriptor.cursor()


runner.execute("SELECT * FROM my_data")
table = runner.fetchall()
for i in table:
	print(i[0])


descriptor.commit()
runner.close()
descriptor.close()