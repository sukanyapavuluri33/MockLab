def add(a, b):
    return a + b

def divide(a, b):
    # This is the bug: it doesn't handle division by zero!
    return a / b
