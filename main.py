import random

def lin():
    print("-"*30)
    print()
def lin2():
    print()
    print("-"*30)

lin()
print("      ESCOLHA UMA OPÇÃO")
lin2()
print()
print("r para rock \np para paper \ns para scissors")
lin2()

def play():
    user = input("SELECIONE SUA OPÇÃO: \n ['r', 'p' or 's']")
    computer = random.choice(['r', 's', 'p'])
    print(computer)

    if user == computer:
        print("EMPATE")
    elif is_win(user, computer):
        print("VOCÊ GANHOU")
    else:
        print("VOCÊ PERDEU")
    
    
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

play()



