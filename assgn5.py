# Design your own class {superhero}

class Superhero:
    def __init__(self, name, secret_identity, powers, weakness, origin_story):
        self.name = name
        self.secret_identity = secret_identity
        self.powers = powers  # This should be a list
        self.weakness = weakness
        self.origin_story = origin_story
        self.energy_level = 100
        
    def use_power(self, power_index):
        if power_index < len(self.powers):
            print(f"{self.name} uses {self.powers[power_index]}!")
            self.energy_level -= 10
        else:
            print("Power not available!")
    
    def take_damage(self, damage_amount, damage_type):
        if damage_type == self.weakness:
            print(f"Critical hit! {self.name} is weak to {damage_type}!")
            self.energy_level -= damage_amount * 2
        else:
            self.energy_level -= damage_amount
            
        if self.energy_level <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} has {self.energy_level} energy remaining.")
    
    def recover(self):
        self.energy_level = min(100, self.energy_level + 25)
        print(f"{self.name} recovers some energy! Now at {self.energy_level}.")
    
    def reveal_identity(self):
        print(f"I am {self.name}, but my secret identity is {self.secret_identity}.")
        print(f"My origin: {self.origin_story}")

# Example usage
spiderman = Superhero(
    name="Spider-Man",
    secret_identity="Peter Parker",
    powers=["Web slinging", "Spider sense", "Wall crawling"],
    weakness="Ethyl chloride",
    origin_story="Bitten by a radioactive spider"
)

spiderman.use_power(0)  # Uses web slinging
spiderman.take_damage(30, "Ethyl chloride")
spiderman.recover()


# Polymorphism challenge (Animal)
class Animal:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Bird(Animal):
    def move(self):
        print(f"{self.name} is flying! 🕊️")

class Fish(Animal):
    def move(self):
        print(f"{self.name} is swimming! 🐠")

class Snake(Animal):
    def move(self):
        print(f"{self.name} is slithering! 🐍")

class Dog(Animal):
    def move(self):
        print(f"{self.name} is running! 🐕")

# Demonstration of polymorphism
animals = [
    Bird("Tweety"),
    Fish("Nemo"),
    Snake("Viper"),
    Dog("Rex")
]

for animal in animals:
    animal.move()