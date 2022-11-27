# love calculator
# take both names
# take both peoples names
# for the first digit count how often the letters of TRUE occur
# for the second digit count how often the letters of TRUE occur

def love_calculator():
    print("Is it true love?")
    name1 = input("Name 1:\n")
    name2 = input("Name 2:\n")
    name1 = name1.lower()
    name2 = name2.lower()
    digit1 = 0
    digit2 = 0
    digit1 += name1.count("t")
    digit1 += name1.count("r")
    digit1 += name1.count("u")
    digit1 += name1.count("e")
    print(name1)
    print(digit1)
