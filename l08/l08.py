import random
def creat_player():
    player = {'hp': 100, 'урон':10}
    player['name'] = input('Введи своё имя, боец: ')
    choose = input('1 - увеличить HP, 2 - увеличить урон')
    if choose == '1':
        player['hp'] += 30
    else:
        player['урон'] += 3
    return player



def show_health(player):
    print('Количество хп:', player['name'], player['hp'])



def attack(attacker, victim):
    damage = random.randint(attacker['урон'] - 3,
    attacker['урон'] + 3)
    print(attacker['name'], 'нанёс', attacker['урон'], ' едениц урона')
    victim['hp'] -= damage



player1 = creat_player()
player2 = creat_player()

while True:
    attack(player1, player2)
    attack(player2, player1)

    show_health(player1)
    show_health(player2)

    if player1['hp'] <= 0:
        print(player2['name'], ' выйграл!')
        break
    if player2['hp'] <= 0:
        print(player1['name'], ' выйграл!')
        break

    input()