import sqlite3

descriptor = sqlite3.connect('DATA.db')
runner = descriptor.cursor()

runner.execute("SELECT * FROM profiles_data")
print(runner.fetchall())

descriptor.commit()
runner.close()
descriptor.close()