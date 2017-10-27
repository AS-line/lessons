class Guns:
	def __init__(self, name, shot_range, calibre, holder, hammer):
		self.name = name
		self.shot_range = shot_range
		self.my_calibre = calibre
		self.holder = holder
		self.hidden_hammer = hammer

	# def show_hummer(self):
	# 	return self.hidden_hammer

	# def change_hammer(self, value):
	# 	print('not change')

	# hammer = property(show_hummer, change_hammer)
	@property
	def my_calibre(self):
		return "Мой калибр " + self.calibre

	@my_calibre.setter
	def my_calibre(self, value):
		self.calibre = value + ' Навальный'

railgun = Guns("Рельсотрон", 200000, "100х200", 1, "USA")
# print(railrun.
# railrun.hammer = "Russa"

railgun.my_calibre = '200x400'
print(railgun.my_calibre)