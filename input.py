# name = input("What is your name?")
# age = int(input("How old are you?"))
# #print(name)
# #print(name, age)
# age_in_dog_years = age * 7
# #print(f"{name} you are {age} years old")
# print (f"{name} you are {age_in_dog_years} in dog years. Wow")

import requests
answer = input("Please enter what you want: ")
parameter = {"rel_rhy": answer}
request = requests.get('https://api.datamuse.com/words',parameter)
rhyme_json = request.json()
for i in rhyme_json[0:3]:
print(i['word'])

