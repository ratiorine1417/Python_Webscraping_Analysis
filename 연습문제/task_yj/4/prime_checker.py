number = int(input('숫자를 입력하세요: '))

if (number < 1):
    print('잘못된 숫자를 입력했습니다. 자연수를 입력해 주세요.')
    exit()
elif number == 1:
    print(f'{number} 은/는 소수가 아닙니다.')
    exit()
elif number == 2:
    print(f'{number} 은/는 소수입니다.')
    exit()
else:
    for i in range(2, number, 1):
        if (number % i) == 0:
            print(f'{number} 은/는 소수가 아닙니다.')
            break
        else:
            print(f'{number} 은/는 소수입니다.')
            break