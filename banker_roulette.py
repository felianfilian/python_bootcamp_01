import random

def banker_roulette():
    print("banker roulette")
    names = input("what are the names:\n")
    name_list = names.split(",")
    picked = random.randint(0, len(name_list)-1)

    print(name_list[picked] + " pay the bill")