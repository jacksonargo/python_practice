# Some oopsie scenarios that might happen

# Infinite recursions

def hello_there():
    print("hello_there")
    hello_there()


hello_there()

# Infinite loops

while True:
    print("hello")
