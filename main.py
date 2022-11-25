print("python bootcamp");


# tip calculator

bill = int(input("what is the total bill\n"))
tip = int(input("how much tip\n"))
people = int(input("how many people\n"))
bill_pp = bill * (1+(tip/100)) / people

print(f"Each person pay: {bill_pp}")
