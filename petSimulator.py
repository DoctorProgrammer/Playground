import random


class Pet:
    def __init__(self, name, animal):
        # attribute have to be set by setter
        self._feed = 5
        self._level = 0.0
        self._name = name
        self._type = animal

    def sleep(self):
        self._feed -= 2
        if self._feed < 0:
            self.die()
            return 1
        return 0

    def play(self):
        self._feed -= 1
        if self._feed < 0:
            return self.die()
        self._level += 0.1
        return 0

    def hit(self):
        self._level -= 0.5
        if self._level < 0:
            return self.flee()
        return 0

    def swim(self):
        self._feed -= 0.5
        chance = 1
        if self._feed < 1:
            chance = 5

        if random.randint(0, 1000) == chance:
            return self.drown()
        if self._feed < 0:
            return self.die()
        return 0

    def die(self):
        print(f"{self._name} died.")
        return 1

    def flee(self):
        print(f"{self._name} fled.")
        return 2

    def drown(self):
        print(f"{self._name} drowned.")
        return 3

    @property
    def name(self):
        return self._name

    @property
    def feed(self):
        return self._feed

    @feed.setter
    def feed(self, value):
        self._feed += value

    @property
    def type(self):
        return self._type

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value

    def __str__(self):
        return f"Name: {self.name}\n" \
            f"\tType: {self.type}\n" \
            f"\tFeed: {self.feed}\n" \
            f"\tLevel: {self.level}\n"


def feed(pet, food):
    pet.feed = food


def choose(list):
    if not pets:
        print("No pets available.")
        return None

    string = "Choose a pet by it's name: \n"
    for pet in list:
        string += f"\t{pet.name} ({pet.type})\n"
    print(string)
    name = input("Enter the name of the pet: ")
    while not find(list, name):
        print("Pet not found.")
        name = input("Enter the name of the pet: ")
    for pet in list:
        if pet.name == name:
            return pet


def find(list, name):
    for pet in list:
        if pet.name == name:
            return True
    return False


def add():
    name = input("Enter the name of the pet: ")
    animal = input("Enter the type of the pet: ")
    return Pet(name, animal)


def pet_action(pet):
    while True:
        action = input("Choose an action (help): ")
        if action == "help":
            print("Available actions: \n"
                  "\tsleep\n"
                  "\tplay\n"
                  "\thit\n"
                  "\tswim\n"
                  "\tfeed\n"
                  "\tstats\n"
                  "\texit\n")
        elif action == "sleep":
            if pet.sleep():
                return 0
        elif action == "play":
            if pet.play():
                return 0
        elif action == "hit":
            if pet.hit():
                return 0
        elif action == "swim":
            if pet.swim():
                return 0
        elif action == "feed":
            feed(pet, int(input("Enter the amount of food: ")))
        elif action == "stats":
            print(pet)
        elif action == "exit":
            break


def start(list):
    while True:
        action = input("Choose an action (help): ")
        if action == "help":
            print("Available actions: \n"
                  "\tadd\n"
                  "\tchoose\n"
                  "\tlist\n"
                  "\texit\n")
        elif action == "add":
            list.append(add())
        elif action == "choose":
            pet = choose(list)
            if pet:
                if pet_action(pet):
                    list.remove(pet)
        elif action == "list":
            for pet in list:
                print("\t" + pet.name)
        elif action == "exit":
            break


if __name__ == '__main__':
    pets = []  # in case you want some default pets, add them here
    print("##### Welcome to pet simulator! #####\n")
    start(pets)
