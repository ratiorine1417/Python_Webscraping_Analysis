def factorial(a):
    if a == 0:
        return 1
    return (a * factorial(a-1))

def repeat(a):
    result = 1
    for i in range(1, a+1):
        result *= i
    return result

fac5 = factorial(5)
rep5 = repeat(5)
fac7 = factorial(7)
rep7 = repeat(7)

print(f'5! (재귀) = {fac5}')
print(f'5! (반복) = {rep5}')
print(f'7! (재귀) = {fac7}')
print(f'7! (반복) = {rep7}')