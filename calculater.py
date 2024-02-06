logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
# Addition
def Addition(n1 ,n2):
    return n1 + n2
# subtraction
def subtract(n1 ,n2):
    return n1 - n2
#multiplication
def multiply(n1 , n2):
    return n1 * n2
# division
def division(n1 , n2):
    return n1/ n2

operators ={
    "+": Addition,
    "-": subtract,
    "*": multiply,
    "/": division
}
print(logo)
num1 = float(input("What's the first number?: "))
for symbol in operators:
    print(symbol)
should_continue = True
while should_continue:

    operators_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the second number?: "))
    calculation_function = operators[operators_symbol]
    first_answer = calculation_function(num1, num2)

    print(f"{num1} {operators_symbol} {num2} = {first_answer}")
    if input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to start a new calculation: ") == 'y':
        num1 = first_answer
    else:
        should_continue = False
        print("Thank you for using online calculater..")
        print("GOOD BYE!....")


