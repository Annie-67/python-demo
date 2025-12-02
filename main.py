# main.py
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

# Initial Feature: Basic Greeting
if __name__ == "__main__":
    print(greet("World"))
    result = add(5, 3)
    print(f"5 + 3 = {result}")