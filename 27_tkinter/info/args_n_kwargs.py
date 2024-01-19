

# Create a func to add as many numbers as user passes as argument

def addNum(*args):
    total = 0
    for num in args:
        total = total + num
    return total

print(addNum(1,2,3,4,5))


def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]    
    print(n)

calculate(2, add=3, multiply=5)