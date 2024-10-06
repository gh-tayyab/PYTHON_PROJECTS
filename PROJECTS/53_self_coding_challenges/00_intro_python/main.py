#Q:1 Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

# 1: Prompt the user to enter the first number.

# 2: Read the input and convert it to an integer.

# 3: Prompt the user to enter the second number.

# 4: Read the input and convert it to an integer.

# 5: Calculate the sum of the two numbers.

# 6: Print the total sum with an appropriate message.

# The provided solution demonstrates a working implementation of this problem, where the main() function guides the user through the process of entering two numbers and displays their sum.



def main():
    print("This program adds two numbers.")
    num1 : str = input("Enter first number: ")
    num1 : int = int(num1)
    num2  : str = input("Enter second number: ")
    num2 : int = int(num2)
    total : int = num1 + num2
    print("The total is " + str(total) + ".")

main()


#Q:2 Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

# Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):

# What's your favorite animal? cow

# My favorite animal is also cow!

animal : str = input("What's your favorite animal? ")
print("My favorite animal is also " + animal + "!")



#Q:3 Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.

# The Celsius scale is widely used to measure temperature, but places still use Fahrenheit. Fahrenheit is another unit for temperature, but the scale is different from Celsius -- for example, 0 degrees Celsius is 32 degrees Fahrenheit!

# The equation you should use for converting from Fahrenheit to Celsius is the following:

# degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

# (Note. The .0 after the 5 and 9 matters in the line above!!!)

# Here's a sample run of the program (user input is in bold italics):

# Enter temperature in Fahrenheit: 76

# Temperature: 76.0F = 24.444444444444443C

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5.0/9.0
print(f"Temperature: {fahrenheit}F = {celsius}C")



#Q:4 Write a program to solve this age-related riddle!

# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

# Anton is 21 years old.

# Beth is 6 years older than Anton.

# Chen is 20 years older than Beth.

# Drew is as old as Chen's age plus Anton's age.

# Ethan is the same age as Chen.

# Your code should store each person's age to a variable and print their names and ages at the end. The autograder is sensitive to capitalization and punctuation, be careful! Your solution should look like this (the below numbers are made up -- your solution should have the correct values!):

# Anton is 3

# Beth is 4

# Chen is 5

# Drew is 6

# Ethan is 7

anton_age = 21
beth_age = anton_age + 6
chen_age = beth_age + 20
drew_age = chen_age + anton_age
ethan_age = chen_age

print(f"Anton is {anton_age}")
print(f"Beth is {beth_age}")
print(f"Chen is {chen_age}")
print(f"Drew is {drew_age}")
print(f"Ethan is {ethan_age}")




#Q:5 Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

# Here's a sample run of the program (user input is in bold italics):

# What is the length of side 1? 3

# What is the length of side 2? 4

# What is the length of side 3? 5.5

# The perimeter of the triangle is 12.5

side1 = float(input("What is the length of side 1? "))
side2 = float(input("What is the length of side 2? "))
side3 = float(input("What is the length of side 3? "))

perimeter = side1 + side2 + side3

print(f"The perimeter of the triangle is {perimeter}")



#Q:6 Ask the user for a number and print its square (the product of the number times itself).

# Here's a sample run of the program (user input is in bold italics):

# Type a number to see its square: 4

# 4.0 squared is 16.0

number = float(input("Type a number to see its square: "))

square = number ** 2

print(f"{number} squared is {square}")