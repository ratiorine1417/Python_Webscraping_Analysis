list_base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_even = [ i for i in list_base if (i%2) == 0 ]
list_square = [ i**2 for i in list_even ]

print(f'원본 리스트: {list_base}')
print(f'짝수들: {list_even}')
print(f'짝수의 제곱: {list_square}')