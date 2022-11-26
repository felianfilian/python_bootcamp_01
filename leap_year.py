
def start():
    year = int(input("Which year to check\n"))

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("a leap year !!!")
            else:
                print("NOT a leap year !!!")
        else:
            print("a leap year !!!")
    else:
        print("NOT a leap year !!!")
