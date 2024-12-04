""" Method 1 """

num = int(input("Give me a number to check: ")) # saņemt numuru
check = int(input("Give me a number to divide by: ")) # iegūstiet skaitli, ar ko dalīt

if num % 4 == 0: # Pārbaudiet, vai varat dalīt skaitli ar 4
    print(num, "is a multiple of 4") # skaitlis ir reizināts ar 4
elif num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")

if num % check == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "doesn't divide evenly by", check)

""" Method 2 """
num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("You picked an odd number.")
else:
    print("You picked an even number.")
