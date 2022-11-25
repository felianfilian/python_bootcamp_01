print("python bootcamp");


# tip calculator

bill = float(input("what is the total bill\n"))
tip = float(input("how much tip\n"))
people = int(input("how many people\n"))
bill_pp = round(bill * (1+(tip/100)) / people)
bill_pp = "{:.2f}".format(bill_pp)
print(f"Each person pay: {bill_pp} €")
