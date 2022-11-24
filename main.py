print("python bootcamp");


# bmi calcuator

height = int(input("your height\n"))
weight = int(input("your weight\n"))
height = height / 100

bmi = round(weight / ((height)**2), 1)

print("Your BMI: \n" + str(bmi))