# tip calculator which calculates the amount every person should after adding tip to the total bill 

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
bill= input("What's total bill? $")
tip = input("how much percent did you want give tip 10,12 and 15 ? ")
total_bill = (float(bill)+(float(bill)*float(tip)/100))
persons = input("how many persons did you want to split the bill? ")
amount = total_bill/int(persons)
print(f"each person should pay ${amount}")