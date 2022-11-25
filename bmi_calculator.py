# bmi calculator version 2

def calc_bmi():
    height = float(input("your height\n"))
    weight = float(input("your weight\n"))

    bmi = weight / ((height/100)**2)
    bmi = round(bmi)

    print("Your BMI:\n" + str(bmi))

    if bmi <= 18.5:
        print("you are underweight")
    elif bmi <= 25:
        print("you are normal weight")
    elif bmi <= 30:
        print("you are overweight")
    elif bmi <= 35:
        print("you are obese")
    else:
        print("your are clinical obese")