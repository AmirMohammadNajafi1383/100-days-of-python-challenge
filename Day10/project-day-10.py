def get_number():
    s = int(input('Enter a number: '))
    return s

def get_operation():
    operation_calculate = ['*', '+', '-', '/']
    for i in operation_calculate:
        print(i)
    
    w = input('Pick an operation: ')
    return w

def get_next_number():
    f =  int(input('Enter the next number: '))
    return f

def calculate(num1 , operator ,num2):
    if operator == '*':
        return num1 + num2
    elif operator == '+':
        return num1 + num2
    elif operator =='-':
        return num1 - num2
    elif operator == '/':
        if num2 != 0 :
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"
    
while True:
    num1 = get_number()
    operator = get_operation()
    num2 = get_next_number()

# Perform the calculation
    result = calculate(num1, operator, num2)

    print(f'{num1} {operator} {num2} = {result}')


    choice = input(f"Type 'y' to continue calculating with {result}, or 'n' to start a new calculation: ") 
    
    if choice.lower() != 'y':
        break

