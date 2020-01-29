# Review questions

# Review Questions
# 1. False
# 2. True
# 3. False
# 4. True
# 5. False
# 6. True, Expressions are fragments of a program that produce data and are made of literals, variables, and operators.
# 7. True
# 8. False, Python does allow the input of multiple values with a single statement
# 9. True
# 10. False, Diamonds represent decision points
#
# Multiple Choice
# 1. C, Fee setting
# 2. A
# 3. D, Specification describes exactly what a computer program will do to solve a problem
# 4. C, Legal identifiers cannot start with numbers.
# 5. B
# 6. B
# 7. B
# 8. D
# 9. A, Assignment in Python is most accurately analogous to a sticky-note
# 10. D
#
# Discussion
# 1. Software development process:
#   a) Understand the problem inside and out
#   b) What will the program accomplish and what it will do, not how it will work. (Inputs/Outputs)
#   c) Create a design in pseudocode
#   d) Implement the design (code)
#   e) Create test cases and debug as necessary piece by piece.
#   f) Maintain and reflect
#
# 2. def main():                                                # Assignment statement
#     print("Chaos function results")                           # Output statement
#     x = [eval(input("Enter a number between 0 and 1: "))]     # x is the identifier / input statement
#     for i in range(100):                                      # i is the identifier / counted loop here
#         x = 3.9 * x * (1 - x)                                 # x is the identifier in the expression
#         print(x)                                              # Output statement
#
# 3. Definite loop is a counted loop (defined in a range). A for loop is a definite loop. A while loop is iterated
#    until condition is met.
#
# 4.
#   a) Gives you the squares of integers 0 through 4 (including 4)
#   b) It will print only a space
#   c) It will print "Hello" four times
#   d) It is iterating powers of 2, starting from 0 to 4.
#
# 5. Forming a plan before implementation reduces bugs in code and will ultimately make a correct working program faster.
#
# 6. sep() function is for controlling separation within a string in a print statement on the same line.
#
# 7. Skip. This is testing literacy.
#
# Programming Exercises
# 1. convert.py
def main1():
    print(
        "Hello there, this is a program that can be used in any instance to quickly convert\nfrom Celsius to Fahrenheit!",
        "\n")
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9 / 5 * celsius + 32
    print("The temperature is", fahrenheit, 'degrees Fahrenheit.')


# 2. convert.py
def main2():
    print(
        "Hello there, this is a program that can be used in any instance to quickly convert\nfrom Celsius to Fahrenheit!",
        "\n")
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9 / 5 * celsius + 32
    print("The temperature is", fahrenheit, 'degrees Fahrenheit.')
    print(input("Press the <Enter> key to quit."))


# 3. avg2.py
def main3():
    print("This program computes the average of two exam scores.")

    score1, score2, score3 = eval(input("Enter three exam scores separated by a comma: "))
    average = (score1 + score2 + score3) / 3

    print("The average of the scores is:", average)


# 4. convert.py
def main4():
    print(
        "Hello there, this is a program that can be used in any instance to quickly convert\nfrom Celsius to Fahrenheit!",
        "\n")
    for i in range(5):
        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = 9 / 5 * celsius + 32
        print("The temperature is", fahrenheit, 'degrees Fahrenheit.')
    print("\nAll done for now!")


# 5. convert.py
# I eliminated the 'fahrenheit' variable, it made more sense to me to eliminate the variable.
def main5():
    print(
        "Hello there, this is a table that can be used in any instance to quickly convert\nfrom Celsius to Fahrenheit!",
        "\n")
    print(input("Press enter to see the table."))
    print("Celsius                           Fahrenheit")
    print("---------------------------------------------")
    for celsius in [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
        print(celsius, "                                  ", (9 / 5 * celsius + 32))
    print("\nAll done for now!")

#6. futval.py
