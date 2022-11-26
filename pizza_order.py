def pizza_order():
    print("Pizza Order")

    size = input("pizza size (s/m/l):\n")
    peperoni = input("add peperoni (y/n):\n")
    cheese = input("extra cheese? (y/n)\n")

    result = 0

    if size == "s":
        result += 15
        if peperoni == "y":
            result += 2
    elif size == "m":
        result += 20
        if peperoni == "y":
            result += 3
    elif size == "m":
        result += 25
        if peperoni == "y":
            result += 3
    else:
        print("wrong size")

    if cheese == "y":
        result += 1

    print(f"pizza price = {result}")