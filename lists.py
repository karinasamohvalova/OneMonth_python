the_count = [1, 2, 3, 4, 5, 6]
the_count.append(7)
the_count.append(8)
the_count.append(9)
the_count.append(10)

# for figure in range(1, 11):
for figure in the_count:
    print("this is count", figure * figure)

stocks = ["APPL", "GOOG", "TSLA"]
for stock in stocks:
    print("Stock ticker:", stock)
#we can go through mixed lists too
random_things = ["puppies", 35, "ivan", 1/2, ["On no", "A list inside the list"]]
for i in random_things:
    print("Here's a random thing:", i)

people = []
people.append("Mattan")
people.append("Sarah")
people.append("Chris")
print(people)
people.remove("Sarah")
print(people)
for person in people:
    print("Person is:", person)


animals = ['bear', 'tiger', 'penguin', 'zebra']
first_animal = animals[0]
print(first_animal)
third_animal = animals[2]
print(third_animal)
print("There are this many things:", len(random_things))
print("this is a:", type(random_things))

another_list = random_things[0]
print(another_list)
print(type(another_list))
another_list_one = random_things[-1]
print(another_list_one)
print(type(another_list_one))