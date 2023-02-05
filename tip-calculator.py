print("Welcome to your tip calculator")
cash = input("What was the total bill? $")
percent = input("What percentage would you like to give? 10, 12 or 15? ")
bill = input("How many people to split the bill? ")


bpercent = int(percent) / 100
percent = float(cash) * float(bpercent)
total = float(cash) + float(percent)
tip = float(total) / int(bill)

print(f"Each person should pay ${round(tip,2)}")
