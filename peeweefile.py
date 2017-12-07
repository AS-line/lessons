import peewee

db = peewee.SqliteDatabase('my_app.db')
#db = peewee

class Book(peewee.Model):
	author = peewee.CharField()
	title = peewee.TextField()

	class Meta():
		database = db

#Book.create_table()
book = Book(author="me", title="Peewee is cool")
book.save()
book2 = Book(author="we", title="Mysql is True")
book2	.save()

for book in Book.select():
	print(book.title)
	print('*'*10)
	print(book.id)