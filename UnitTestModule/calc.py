def add(x,y):
    return x + y

def subtract(x,y):
    if x > y:
        return x - y
    else:
        return y - x

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y