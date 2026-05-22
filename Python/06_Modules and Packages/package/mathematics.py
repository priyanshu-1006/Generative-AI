def addition(a, b):
    return a + b

def subtraction(a, b):
    if a > b:
        return a - b
    else:
        return b - a

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b

