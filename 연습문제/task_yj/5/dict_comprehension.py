dict_square = { key:key**2 for key in range(1,6)}
dict_even_square = { key:key**2 for key in range(1,11) if (key%2) == 0 }
# key:key**2 for key in range(2,11,2)
print(f'1부터 5까지의 제곱 딕셔너리: {dict_square}')
print(f'짝수만의 제곱 딕셔너리: {dict_even_square}')