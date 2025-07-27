import math_operations as mo

radius = 5
length = 10
width = 5
num_f = 5
num1 = 48
num2 = 18

mo.circle(radius)
mo.rectangle(length, width)
result = mo.factorial(num_f)
print(f"팩토리얼 {num_f}! = {result}")
mo.greatest_common_divisor(num1, num2)