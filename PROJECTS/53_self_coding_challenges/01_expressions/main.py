#Q:1 Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

import random

# Function to simulate rolling two dice
def roll_two_dice():
    die1 = random.randint(1, 6)  # Local variable for the first die
    die2 = random.randint(1, 6)  # Local variable for the second die
    return die1, die2

# Main code
for i in range(1, 4):  # Loop 3 times to simulate 3 rolls
    # Each call to roll_two_dice has local scope for die1 and die2
    die1, die2 = roll_two_dice()
    print(f"Roll {i}: Die 1 = {die1}, Die 2 = {die2}")



#Q:2 Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

# E = m * c**2

# Almost 100 years ago, Albert Einstein famously discovered that mass and energy are interchangeable and are related by the above equation. You should ask the user for mass (m) in kilograms and use a constant value for the speed of light -- C = 299792458 m/s.

# Here's a sample run of the program (user input is in bold italics):

# Enter kilos of mass: 100

# e = m * C^2...

# m = 100.0 kg

# C = 299792458 m/s

# 8.987551787368176e+18 joules of energy!C = 299792458  # Speed of light in meters per second

C = 299792458

while True:
    mass = float(input("Enter kilos of mass (or type 0 to exit): "))

    if mass == 0:
        print("Exiting the program.")
        break

    energy = mass * C ** 2

    print("\ne = m * C^2...")
    print(f"m = {mass} kg")
    print(f"C = {C} m/s")
    print(f"{energy} joules of energy!\n")




#Q:3 Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

INCHES_PER_FOOT = 12

feet = float(input("Enter the number of feet: "))

inches = feet * INCHES_PER_FOOT

if feet == 1:
    print(f"{feet} foot is equal to {inches} inches.")
else:
    print(f"{feet} feet are equal to {inches} inches.")





#Q:4 Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

# The Pythagorean theorem, named after the ancient Greek thinker, Pythagoras, is a fundamental relation in geometry. It states that in a right triangle, the square of the hypotenuse is equal to the sum of the square of the other two sides.

# For instance, let's consider a right triangle ABC, with the right angle located at C. According to the Pythagorean theorem:

# BC ** 2 = AB ** 2 + AC ** 2

# Your code should read in the lengths of the sides AB and AC, and that outputs the length of the hypotenuse (BC). You will probably find math.sqrt() to be useful.

# Here's a sample run of the program (user input is in bold italics):

# Enter the length of AB: 3

# Enter the length of AC: 4

# The length of BC (the hypotenuse) is: 5.0

import math

ab = float(input("Enter the length of AB: "))
ac = float(input("Enter the length of AC: "))

bc = math.sqrt(ab**2 + ac**2)

print("The length of BC (the hypotenuse) is:", bc)





#Q:5 Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

# Here's a sample run of the program (user input is in bold italics):

# Please enter an integer to be divided: 5

# Please enter an integer to divide by: 3

# The result of this division is 1 with a remainder of 2

num1 = int(input("Please enter an integer to be divided: "))
num2 = int(input("Please enter an integer to divide by: "))
print("The result of this division is", num1 // num2, "with a remainder of", num1 % num2)





#Q:6 Simulate rolling two dice, and prints results of each roll as well as the total.

import random

print('Rolling the dice...')
print('The values are:')
print(random.randint(1, 6))
print(random.randint(1, 6))





#Q:7 Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):

# There are 5 seconds in a year!

# You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.

DAYS_IN_YEAR = 365
HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60
SECONDS_IN_MINUTE = 60

seconds_in_year = DAYS_IN_YEAR * HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE

print(f"There are {seconds_in_year} seconds in a year!")





#Q:8 Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

# Mad Libs is a word game where players are prompted for one word at a time, and the words are eventually filled into the blanks of a word template to make an entertaining story! We've provided you with the beginning of a sentence (the SENTENCE_START constant) which will end in a user-inputted adjective, noun, and then verb.

# Here's a sample run (user input is in bold italics):

# Please type an adjective and press enter. tiny

# Please type a noun and press enter. plant

# Please type a verb and press enter. fly

# Code in Place is fun. I learned to program and used Python to make my tiny plant fly!

SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my"

adjective = input("Please type an adjective and press enter: ")
noun = input("Please type a noun and press enter: ")
verb = input("Please type a verb and press enter: ")

print(f"{SENTENCE_START} {adjective} {noun} {verb}!")