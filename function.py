def greet(name):
    return f"Hey {name}!"
print(greet('Mattan'))

def concatenate(word_one, word_two):
    return word_one + word_two
print(concatenate('lo', 've'))

def age_in_dog_years(age):
    return age * 7
print(age_in_dog_years(28))


name = "Mattan"
def print_different_name():
    name = "Chris"
    print(name)

print(name)
print_different_name()
print(name)


def uppercase_and_reverse(string):
    return string [::-1]. upper()
print(uppercase_and_reverse("banana"))