number = int(input('몇 단을 출력할까요? '))
if (number > 0)&(number < 10):
    print('7단 구구단:')
    for i in range(1, 10, 1):
        print(f'{number} x {i} = {number*i}')
else:
    print('구구단을 출력하는 프로그램입니다. (1~9) 숫자 중 하나를 입력해 주세요.')