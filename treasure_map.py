def treasure_map():
    print("treasure map")
    row1 = ["■", "■", "■"]
    row2 = ["■", "■", "■"]
    row3 = ["■", "■", "■"]

    map = [row1, row2, row3]
    print(f"{row1}\n{row2}\n{row3}\n")
    position = input("Where do you want to put the treasure?\n")
    pos_x = int(position[1]) -1
    pos_y = int(position[0]) -1
    map[pos_x][pos_y] = "X"
    print(f"{row1}\n{row2}\n{row3}\n")