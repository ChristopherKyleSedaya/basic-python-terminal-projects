from art import logo
print(logo)
# Basic operations
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Storing the functions in a dictionary

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


running = True
continue_operation = 0
continue_with_first_result = ""
num1 = float(input("Type your first number"))
while running :
    if continue_with_first_result == "n":
        num1 = float(input("Type your first number"))
    operator = input("What operation? \n + \n - \n * \n / \n")
    num2 = float(input("What is your second number?"))

    process_operation = operations[operator](num1, num2)
    print(f"{num1} {operator} {num2} = {process_operation}")
    continue_operation = process_operation

    continue_with_first_result = input(f"Type 'y' to continue calculating with {continue_operation} or type 'n' to start a new calculation \n or type 'stop' to stop program ").lower()

    if continue_with_first_result == "y":

        num1 = continue_operation
    elif continue_with_first_result == "stop":
        print("Goodbye!")
        running = False
