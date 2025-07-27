number = 1
sum = 0

while number:
    number = int(input('숫자를 입력하세요 (0을 입력하면 종료): '))
    sum += number
print(f'입력된 숫자들의 합: {sum}')