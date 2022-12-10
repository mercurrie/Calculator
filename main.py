from art import logo

# add function
def add(n1,n2):
    return n1 + n2

# subtract function
def subtract(n1,n2):
    return n1 - n2

# multiply function
def multiply(n1,n2):
    return n1 * n2

# divide function
def divide(n1,n2):
    return n1/ n2

# sqrRoot function
def sqrRoot(n1,n2):
    if n2.is_integer():
        n2 = int(n2)
        count = n1
        for num in range(1, n2):
            count *= n1
        return count
    else:
        print("n\ERROR: operation currently only available with whole numbers")
        calculation()
        
# operation dictionary
operations = {"+": add,
            "-": subtract,
            "*": multiply,
            "/": divide,
            "^": sqrRoot}

# Calculate function: takes in inputs and outputs calculation
def calculation():
    # print logo
    print(logo)
    
    num1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)

    # while loop to continue additional calculations
    end = True
    while end:
        operationSymbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        calculate = operations[operationSymbol]
        answer = calculate(num1,num2)
        print(f"{num1} {operationSymbol} {num2} = {answer}")
        repeat = input(f"Type 'y' to continue claculating with {answer}, type 'n' to start a new calculation: ")
        
        if repeat == 'y':
            num1 = answer
        else:
            end = False
            calculation()
        
# call calculation function
calculation()