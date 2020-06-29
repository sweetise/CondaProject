# Numbers
# Strings
# Booleans

#Define "Person" type with "name attribute" and "talk method"
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def talk(self):
        print(f"Hi, I am {self.firstname}. I come to chew bubblegum. ")

john = Person("Jonathan" , "Smith")
print(f"{john.firstname}'s last name is {john.lastname}")
john.talk()

bob = Person("Bob" , "Walker")
print("\n" f"{bob.firstname}'s last name is {bob.lastname}")
bob.talk()