print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip do you wanna pay, 10, 12 or 15? %"))
total_persons = int(input("How many of you were there? "))
tip1 = (tip * bill) / 100
total = bill + tip1
each_person = total/total_persons

print(f"Each person should pay ${each_person:.2f} ")


