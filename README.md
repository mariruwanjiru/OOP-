📘 Assignment 1 & Activity 2: Python OOP – Class Design & Polymorphism
This project showcases foundational Object-Oriented Programming (OOP) concepts in Python by completing two challenges:

Assignment 1: Design Your Own Class

Activity 2: Polymorphism Challenge

The goal is to understand classes, objects, inheritance, constructors, encapsulation, and polymorphism through practical examples.

🧠 Concepts Covered
✅ Class and Object Creation

✅ Constructors (__init__)

✅ Inheritance

✅ Method Overriding

✅ Encapsulation (protected attributes)

✅ Polymorphism

🏗️ Assignment 1: Design Your Own Class – Superhero Universe
We created a base class Superhero and derived two specialized subclasses:

FlyingHero: Represents heroes with flying abilities.

TechHero: Represents heroes who use technology-based powers.

Each class:

Initializes attributes like name, power, and universe using a constructor.

Demonstrates encapsulation using a protected _power attribute.

Overrides the use_power() method to reflect unique behaviors.

🔍 Example Output:
text
Copy
Edit
🦸 Superhero: Skyhawk
🌌 Universe: AeroVerse
💥 Power: Flight
Skyhawk soars into the sky with Flight!

🦸 Superhero: TechNova
🌌 Universe: CyberRealm
💥 Power: Advanced AI
TechNova deploys high-tech gadgets with Advanced AI!

🎭 Activity 2: Polymorphism Challenge – Vehicles in Motion
This activity demonstrates polymorphism using a base class Vehicle and its subclasses:

Car
Boat
Plane

Each class defines its own version of the move() method. Even though the method name is the same, the behavior is unique to each subclass — a core principle of polymorphism.

🔍 Example Output:
🚗 Driving on the road.
🚤 Sailing on water.
✈️ Flying in the sky.

🗂️ File Structure
.
├── Superhero_Class.py       # Contains Assignment 1 solution
├── Polymorphism_Activity.py # Contains Activity 2 solution
└── README.md                # Project description and explanation

🚀 How to Run
Make sure you have Python installed.

Run each file in your terminal or editor:
python Superhero_Class.py
python Polymorphism_Activity.py

🙌 Final Thoughts
This project helps reinforce the core building blocks of OOP in Python. It prepares you for more advanced topics like abstraction, interfaces, and design patterns. Use these examples as templates for your future projects!
