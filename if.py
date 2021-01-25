Conditional statements


answer = input("Do you want to hear a joke? ")
if answer == "Yes" or answer == "yes":
    print("I'm against picketing, but I don't know how to show it.")
elif answer == "No" or answer == "no":
    print("Ok.")
else:
    print("I can't understand you.")


answer = input("Do you want to hear a joke? ")
affirmative_responses = ["yes", "Yes", "Y", "y"]
negative_responses = ["No", "no", "n", "N"]
if answer in affirmative_responses : 
	print("I'm against picketing, but I don't know how to show it.")
elif answer in negative_responses :
    print("Ok.")
else:
    print("I can't understand you.")


answer = input("Do you want to hear a joke? ")
affirmative_responses = ["yes", "y"]
negative_responses = ["no", "n"]
if answer. lower() in affirmative_responses : 
    print("I'm against picketing, but I don't know how to show it.")
elif answer. lower() in negative_responses :
    print("Ok.")
else:
    print("I can't understand you.")


answer = input("Do you want to hear a joke? ")
if "y" in answer. lower() : 
    print("I'm against picketing, but I don't know how to show it.")
elif "n" in answer. lower() :
    print("Ok.")
else:
    print("I can't understand you.")



