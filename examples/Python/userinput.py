name = input("Hey person, what is your name? ")
print(name)

while True:
    name = input("Hey person, what is your name? ")
    if name.isalpha():
        break
