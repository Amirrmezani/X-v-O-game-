import random


def show():
    for i in range(0, 9):
        print(game[i], end=' ')
        if i == 2 or i == 5:
            print()
    print()


def check():
    b = False
    # -----------------row  system------------------------------
    if game[0] == 'x' and game[1] == 'x' and game[2] == 'x':
        print('win system ')
        b = True
    if game[3] == 'x' and game[4] == 'x' and game[5] == 'x':
        print('win system ')
        b = True
    if game[6] == 'x' and game[7] == 'x' and game[8] == 'x':
        print('win system ')
        b = True
    # -----------------row  you------------------------------
    if game[0] == 'o' and game[1] == 'o' and game[2] == 'o':
        print('win you ')
        b = True
    if game[3] == 'o' and game[4] == 'o' and game[5] == 'o':
        print('win you ')
        b = True
    if game[6] == 'o' and game[7] == 'o' and game[8] == 'o':
        print('win you ')
        b = True
    # -----------------col  you------------------------------
    if game[0] == 'o' and game[3] == 'o' and game[6] == 'o':
        print('win you ')
        b = True
    if game[1] == 'o' and game[4] == 'o' and game[7] == 'o':
        print('win you ')
        b = True
    if game[2] == 'o' and game[5] == 'o' and game[8] == 'o':
        print('win you ')
        b = True
    # -----------------col  system------------------------------
    if game[0] == 'x' and game[3] == 'x' and game[6] == 'x':
        print('win system ')
        b = True
    if game[1] == 'x' and game[4] == 'x' and game[7] == 'x':
        print('win system ')
        b = True
    if game[2] == 'x' and game[5] == 'x' and game[8] == 'x':
        print('win system ')
        b = True
    # -----------------ghotr  system------------------------------
    if game[0] == 'x' and game[4] == 'x' and game[8] == 'x':
        print('win system ')
        b = True

    if game[2] == 'x' and game[4] == 'x' and game[6] == 'x':
        print('win system ')
        b = True
    # -----------------ghotr  you------------------------------
    if game[0] == 'o' and game[4] == 'o' and game[8] == 'o':
        print('win you ')
        b = True

    if game[2] == 'o' and game[4] == 'o' and game[6] == 'o':
        print('win you ')
        b = True
    if game.count('-') == 0:
        print('end game :( ')
        b = True
    return b
# -----------------------------------------------


game = []

for i in range(0, 9):
    game.append('-')
# -----------------------------------------------
show()
print('-'*20)
# -----------------------------------------------
while True:
    if check():
        break
    s = random.randint(0, 8)
    if game[s] == '-':
        game[s] = 'x'
    show()
    print('-' * 20)
    # -----------------------------------------------
    if check():
        break
    s = int(input('o  => num (0 ..8 ) :'))
    if game[s] == '-':
        game[s] = 'o'
    show()
    print('-' * 20)

