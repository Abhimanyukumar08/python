''''Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:
'''


age = int(input("What is your current age:? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_remaining = 90 - age
days_remaining = age_remaining * 365
weeks_remaining = age_remaining * 52
months_remaining = age_remaining * 12
print(f"You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months are left") 
