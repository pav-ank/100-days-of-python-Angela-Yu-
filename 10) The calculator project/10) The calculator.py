import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return  n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    print(art.logo)
    should_continuation = True
    n1 = float(input("Enter the first number: "))

    while should_continuation:
        for symbols in operations:
            print(symbols)
        symbol = input("What would you like to perform?: ")

        n2 = float(input("Enter the second number: "))

        result = operations[symbol](n1, n2)
        print(f"{n1} {symbol} {n2} = {result}")

        continuation = input(f"Would you like to continue with {result}? type 'y' to continue or 'n' to exit: ").lower()
        if continuation == 'y':
            n1 = result
        elif continuation == 'n':
            should_continuation = False
            print("\n" * 200)
            calculator() #to continue with new calculations incase the user types 'n'.
        else:
            break
calculator()