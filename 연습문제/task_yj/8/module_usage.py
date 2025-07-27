import datetime
import random

def generate_data():
    now = datetime.datetime.now()
    print(f"현재 날짜와 시간: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    
    weekday = { 0: '월요일', 1: '화요일', 2: '수요일', 3: '목요일',
               4: '금요일', 5: '토요일', 6: '일요일'}
    index_w = now.weekday()
    
    print(f"포맷된 날짜: {now.strftime('%Y년 %m월 %d일')} {weekday[index_w]}")

    random_int = random.randint(1, 10)
    print(f"임의의 숫자: {random_int}")

    random_float = random.uniform(1.0, 5.0)
    print(f"임의의 실수: {random_float:.2f}")

    fruits = ['사과', '바나나', '오렌지', '딸기', '포도']
    random_fruit = random.choice(fruits)
    print(f"임의의 리스트 요소: {random_fruit}")

    random.shuffle(fruits)
    print(f"섞인 리스트: {fruits}")

generate_data()