import random

def heads_tails():
    print("heads or tails")
    coin = random.randint(0, 1)
    if coin == 0:
        print("head")
    if coin == 1:
        print("tail")
