print("WELCOME TO THE TIP CALCULATOR")

bill = float(input("What was the total bill? $"))
tip  = int(input("How much percentage of tip would you like to give? 10,12,or 15: "))
people = int(input("How many people are there: "))
total_amount = float(bill + (tip/100 *bill))
bill__per_person = round(total_amount/people,2)
print(f"the total amount after addding the tip is {total_amount} , and the bill per head will be {bill__per_person}" )
