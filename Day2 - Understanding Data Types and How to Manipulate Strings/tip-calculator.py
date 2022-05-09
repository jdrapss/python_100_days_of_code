#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Welcome to the tip calculator!
# What was the total bill? $124.56
# How much tip would you like to give? 10, 12, or 15? 12
# How many people to split the bill? 7

#Write your code below this line 👇

print("Welcome to the tip Calculator!\n")
total_bill = float(input("What was the total bill? $")) # 150
tip = int(input("How much tip would you like to give? 10, 15, 20, or 25? ")) # 12.0
bill_split = int(input("How many people to split the bill? ")) # 5

tip_calculation = (tip / 100) + 1
# bill_with_tip = tip / 100 * total_bill + total_bill
# print(bill_with_tip)
total_tip = float((total_bill * tip_calculation - total_bill))
each_person_total = float((total_bill * tip_calculation) / bill_split)

#eptr = round(each_person_total,2)
final_amount = (round(each_person_total,2))
final_amount = "{:.2f}".format(each_person_total) # allows me to force two decimal places for a specific variable
#print(eptr)

print(f"Each person should pay: ${final_amount} and each person should tip ${round(total_tip, 2)}.")