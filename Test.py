
print()
print(" Вводные данные соответсвуют индексу")
print()
print("---------------------------")
print(" ---- Крестики-нолики ---- ")
print("---------------------------")

field = list(range(1,10))
def show_board(fiend):
    print ()
    print("-------------")
    for i in range(3):
        print ("|", field[0+i*3], "|", field[1+i*3], "|", field[2+i*3], "|")
        print ("-------------")

def motion(player):
   while True:
       step = input(" Ваш ход:  ")
       if not (step in "123456789"):
           print(" Некорректные данные. Повторите ввод:"   )
           continue
       if len(step) != 1:
           print("Введите одну координату")
           continue
       step = int(step)
       if str(field[step - 1]) in "XO":
           print("Эта клетка занята: ")
           continue
       field[step - 1] = player
       break

def check_win(field):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for i in win_coord:
       if field[i[0]] == field[i[1]] == field[i[2]]:
          return field[i[0]]
   return False

def game(field):
    counter = 0
    while True:
        show_board(field)
        if counter % 2 == 0:
           motion("X")
        else:
           motion("O")
        counter += 1
        if counter > 4:
           value = check_win(field)
           show_board(field)
           if value:
              print(f"Игравший за {value} выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break

game(field)

