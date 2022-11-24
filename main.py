print("python bootcamp");


# life in weeks

age = int(input("What is your age: \n"))
age_left = 90 - age
total_days = age_left * 365
total_weeks = round(age_left * 52)
total_month = round(age_left * 12)

print(f"You have {total_days} days, {total_weeks} weeks and {total_month} months left!")