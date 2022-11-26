def pizza_order():
    print("Pizza Order")

    size = input("pizza size (s/m/l):\n")
    peperoni = input("add peperoni (y/n):\n")
    cheese = input("extra cheese? (y/n)\n")

    result = 0

    if size == "s":
        result += 15
    elif size == "m":
        result += 20
    elif size == "m":
        result += 25
    else:
        print("wrong size")

    if peperoni == "y":
        result += 2

    if cheese == "y":
        result += 1

    print(f"pizza price = {result}")