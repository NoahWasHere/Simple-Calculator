#Simple calculator writen in python3.
import sys


class operations:
    def add(n1, n2):
        return n1 + n2
    
    def multiply(n1, n2):
        return n1 * n2
    
    def subtract(n1, n2):
        return n1 - n2
    
    def divide(n1, n2):
        return n1 / n2

print('''Operations:
1 - Add
2 - Subtract
3 - Multiply
4 - Divivde''')

while True:
    chosen_operation = input('Enter an operation (1, 2, 3, 4): ')

    number1 = float(input('Enter the first number: '))
    number2 = float(input('Enter the second number: '))

    if chosen_operation == '1':
        print("Ans:")
        print(operations.add(number1, number2))

    elif chosen_operation == '2':
        print("Ans:")
        print(operations.subtract(number1, number2))

    elif chosen_operation == '3':
        print("Ans:")
        print(operations.multiply(number1, number2))

    elif chosen_operation == '4':
        print("Ans:")
        print(operations.divide(number1, number2))

    else:
        print("ERROR: Invalid operation.")
