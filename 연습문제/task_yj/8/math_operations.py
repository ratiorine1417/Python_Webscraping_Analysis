import math

def circle(r):
    print(f"원의 넓이: {math.pi * (r**2):.2f}")
    # return (math.pi * (r**2))

def rectangle(length, width):
    print(f"직사각형 넓이: {length * width}")
    # return length * width

def factorial(n):
    if n == 0:
        return 1
    else:
        return math.factorial(n) # n * factorial(n-1)

def greatest_common_divisor(a, b):
    print(f"최대공약수({a}, {b}) = {math.gcd(a, b)}")
    # return math.gcd(a, b)