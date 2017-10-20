def ride(car):
	car['distance'] +=car['speed']
	car['fuel'] -= car['spend']

def faster(car):
	car['speed'] += 2
	car['spend'] += 2

def nitro(car):
	car['distance'] += car['nitro']
	car['fuel'] -= car['spend'] * 3

def car_info(car):
	print('\n Текущее состояние: ',
		'Топливо: ' + str(car['fuel']),
		'Скорость: ' + str(car['speed']),
		'Проехали: ' + str(car['distance']) + '/' + str(track))
		

def race_step(car):# надо вызвать
	choose = input('Твой ход,' + car['name'] + "Что будем делать?")
	if choose == '1':
		ride(car)
	elif choose == '2':
		faster(car)
	elif choose == '3':
		nitro(car)
	car_info(car)
	input()



racer1 = {
	'name': 'Чайка',
	'speed': 5,
	'fuel': 25,
	'spend': 2,
	'nitro': 8,
	'distance': 0
}


racer2 = {
	'name': 'Ниво',
	'speed': 3,
	'fuel': 35,
	'spend': 2,
	'nitro': 8,
	'distance': 0
}


racer3 = {
	'name': 'Шиха',
	'speed': 6,
	'fuel': 30,
	'spend': 5,
	'nitro': 10,
	'distance': 0,
}


track = 40

while True:
	race_step(racer1)
	race_step(racer2)