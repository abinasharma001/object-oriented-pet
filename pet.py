# Create an object-oriented virtual pet.
# The pet has a name, hunger level, and happiness level.
# Includes methods to feed the pet, play with the pet, and display its status.

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5      # 0 = not hungry, 10 = very hungry
        self.happiness = 5   # 0 = sad, 10 = very happy

    def feed(self):
        if self.hunger > 0:
            self.hunger -= 1
        print(f"{self.name} has been fed.")

    def play(self):
        if self.happiness < 10:
            self.happiness += 1
        self.hunger += 1
        print(f"You played with {self.name}.")

    def getStatus(self):
        print("\nPet Status")
        print(f"Name: {self.name}")
        print(f"Hunger Level: {self.hunger}/10")
        print(f"Happiness Level: {self.happiness}/10")


# --- Simple demo ---
pet_name = input("Enter your pet's name: ")
my_pet = Pet(pet_name)

my_pet.getStatus()
my_pet.feed()
my_pet.play()
my_pet.getStatus()
