import random

def rock_paper():
    print("rock paper")
    signs = ["rock", "paper", "scissors"]
    sign = int(input("rock (0) paper (1) scissors (2)\n"))
    ai_sign = random.randint(0, 2)

    if sign >= 3 or sign < 0:
        print("invalid number  - you loose")
    else:
        print(signs[sign] + " VS " + signs[ai_sign])

        if sign == ai_sign:
            print("draw")
        elif sign == 0 and ai_sign == 1:
            print("you loose")
        elif sign == 0 and ai_sign == 2:
            print("you win")
        elif sign == 1 and ai_sign == 0:
            print("you win")
        elif sign == 1 and ai_sign == 2:
            print("you loose")
        elif sign == 2 and ai_sign == 0:
            print("you loose")
        elif sign == 2 and ai_sign == 1:
            print("you win")
