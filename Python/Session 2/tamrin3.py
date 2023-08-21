def add(a1, a2):
    return a1 + a2


def minus(a1, a2):
    return a1 - a2


def multiply(a1, a2):
    return a1 * a2


def divide(a1, a2):
    return a1 / a2


number1 = int(input("Enter Number 1:"))
number2 = int(input("Enter Number 2:"))

print("Add ->", add(number1, number2))
print("Minus ->", minus(number1, number2))
print("Multiply ->", multiply(number1, number2))
print("Divide ->", divide(number1, number2))
