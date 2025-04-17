# Base class
class Superhero:
    def __init__(self, name, power, universe):
        self.name = name
        self._power = power  # Encapsulated with a leading underscore
        self.universe = universe

    def display_info(self):
        print(f"🦸 Superhero: {self.name}")
        print(f"🌌 Universe: {self.universe}")
        print(f"💥 Power: {self._power}")

    def use_power(self):
        print(f"{self.name} uses {self._power}!")

# Subclass 1
class FlyingHero(Superhero):
    def use_power(self):
        print(f"{self.name} soars into the sky with {self._power}!")

# Subclass 2
class TechHero(Superhero):
    def use_power(self):
        print(f"{self.name} deploys high-tech gadgets with {self._power}!")

# Create objects
hero1 = FlyingHero("Skyhawk", "Flight", "AeroVerse")
hero2 = TechHero("TechNova", "Advanced AI", "CyberRealm")

# Call methods
hero1.display_info()
hero1.use_power()

print()  # Separator

hero2.display_info()
hero2.use_power()
