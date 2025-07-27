fruit = ['사과', '바나나', '오렌지', '포도', '딸기']

print(f'과일 목록: {fruit}')
look_for = input('찾을 과일을 입력하세요: ')

if look_for in fruit:
    print(f"'{look_for}'가 목록에 있습니다!")
else:
    print(f"'{look_for}'가 목록에 없습니다!")
