numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter_numbers = list(filter(lambda x: x>5, numbers))

print(f'원본 숫자: {numbers}')
print(f'모든 수의 제곱: {list(map(lambda x: x**2, numbers))}')
print(f'5보다 큰 수들: {filter_numbers}')
print(f'5보다 큰 수들의 제곱: {list(map(lambda x: x**2, filter_numbers))}')