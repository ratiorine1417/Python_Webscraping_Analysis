numbers1 = [2, 4, 6, 8, 10]
numbers2 = [1, 3, 5, 7, 12]

print(f'숫자 리스트: {numbers1}')
print(f'모든 수가 짝수인가? {all((number%2) == 0 for number in numbers1)}')
print(f'하나라도 10보다 큰 수가 있는가? {any(number > 10 for number in numbers1)}')

print(f'숫자 리스트2: {numbers2}')
print(f'모든 수가 짝수인가? {all((number%2) == 0 for number in numbers2)}')
print(f'하나라도 10보다 큰 수가 있는가? {any(number > 10 for number in numbers2)}')