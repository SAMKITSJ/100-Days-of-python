# program to print how much time you have left to live until 90 years old 

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
years = 90 - int(age)
months = int(years * 12)
weeks = int(years * 52)
days = int(years * 365)
print(f"you have {days} days, {weeks}weeks, and {months} months left.")



