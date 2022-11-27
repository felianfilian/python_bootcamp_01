# love calculator
# take both names
# take both peoples names
# for the first digit count how often the letters of TRUE occur
# for the second digit count how often the letters of TRUE occur

def love_calculator():
    print("Is it true love?")
    name1 = input("Name 1:\n")
    name2 = input("Name 2:\n")
    combined_names = name1 + name2
    combined_names = combined_names.lower()
    digit1 = 0
    digit2 = 0

    digit1 += combined_names.count("t")
    digit1 += combined_names.count("r")
    digit1 += combined_names.count("u")
    digit1 += combined_names.count("e")

    if digit1 >= 10:
        digit1 = 10

    digit2 += combined_names.count("l")
    digit2 += combined_names.count("o")
    digit2 += combined_names.count("v")
    digit2 += combined_names.count("e")

    if digit1 >= 10:
        digit1 = 10

    lovescore = digit1 + digit2

    print(name1 + " " + name2)
    print("Lovescore = " + str(lovescore))
    if (lovescore < 10) or (lovescore > 90):
        print("you go together perfectly")
    if (lovescore >= 40) or (lovescore <= 40):
        print("you go together very well")
