# Dictionary - {}
# List - []
states = {'NY': 'New york', 'PA': 'Pennsylvania', 'CA': 'California'}
states['FL'] = 'Florida' #append
print(states)

print(states['NY'])
print(type(states))
# print(states.get('FL', 'Not found'))
print(states.get('PA', 'Not found'))
print(states.keys())
print(states.values())


user = {'name': 'Karina', 'height': 55, 'shoe sixe': 10.5, 'hair': 'Brown', 'eyes': 'Brown'}
blog = {'title': 'Wooow', 'body': 'Blaa'}
print(user['name'])
print(blog['title'])

animal_sounds = {'cat': ['meow', 'purr'],'dog': ['bark', 'gav'], 'fox': []}
print(animal_sounds)

kira = {'name': 'Kira', 'height': 57, 'shoe sixe': 10.5, 'hair': 'Brown', 'eyes': 'Brown'}
ivan = {'name': 'Ivan', 'height': 59, 'shoe sixe': 11, 'hair': 'Brown', 'eyes': 'Brown'}
ilona = {'name': 'Ilona', 'height': 55, 'shoe sixe': 10.5, 'hair': 'Brown', 'eyes': 'Brown'}
people = [kira, ivan, ilona]
print(people)
for person in people:
    print(person['height'])