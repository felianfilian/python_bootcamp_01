print("python bootcamp");


# tip calculator

bill = float(input("what is the total bill\n"))
tip = float(input("how much tip\n"))
people = int(input("how many people\n"))
bill_pp = bill * (1+(tip/100)) / people

print(f"Each person pay: {round(bill_pp, 2)} €")
