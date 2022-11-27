def treasure_island():
    print("welcome to treasure island")

    i = 1
    while i != 0:
        if i != 1:
            i = int(input())
        if i == 1:
            print("you came to a cave a stepped into it. you can choose the left (2) oder the right (3) tunnel")
            i = int(input())
        if i == 2:
            print("a big ogre smashed you down - Game Over")
            i = 0
        if i == 3:
            print(
                "You arrive a big lake. A boat with an skeleton ferryman is coming. Do you like to wait (4) for the ferryman or do you rather choose to swim(5)")
        if i == 4:
            print("The ferryman arrives the riverbank. and offer you a ride for 1 goldcoin")
            i = 0
        if i == 5:
            print("you swim some hundred meters until somethings pulls you under the water - Game Over")
            i = 0
    print("game ended")

