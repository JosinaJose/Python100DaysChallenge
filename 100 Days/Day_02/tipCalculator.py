print("Welcome to Tip Calculation!")
total_bill = float(input("What was the  total bill: "))
tip_percentage =int(input("How much tip would you like to give? 10, 12, or 15: "))
num_people=int(input("How many people to split the bill: "))
tip = float(tip_percentage/100) * total_bill + total_bill
#print(tip)
total_amt_perPerson = tip / num_people
final_amt =round(total_amt_perPerson, 2)
print(f"Each person should pay: ${final_amt}" )