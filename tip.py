# We ask client's name and his bill
name = input("What is your name? ")
original_bill = int(input("What is your bill? "))

# We count three types if tips
tip_one = original_bill * 0.15
tip_two = original_bill * 0.18
tip_three = original_bill * 0.20

# We make an offer to the person. It includes 3 choices.
print("You can choose one of three types of tips")
print(f"{name} 15% tip from your bill is ${tip_one:.1f}.")
print(f"{name} 18% tip from your bill is ${tip_two:.1f}.")
print(f"{name} 20% tip from your bill is ${tip_three:.1f}.")
