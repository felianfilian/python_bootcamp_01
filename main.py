print("python bootcamp");


# bmi calculator version 2
height = float(input("your height\n"))
weight = float(input("your weight\n"))

bmi = weight / ((height/100)**2)
bmi = round(bmi)

print("Your BMI:\n" + str(bmi))