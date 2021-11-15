from _typeshed import Self


class Pet():
    def __init__(self):
        self.name = "lucy"

    def say_name(self):
        print(self.name)


my_pet = Pet()
print(my_pet.say_name())
