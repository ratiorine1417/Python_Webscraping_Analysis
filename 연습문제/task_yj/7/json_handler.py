import pandas as pd

person1 = {'이름': '김철수', '나이': 25, '직업': '개발자',
           '취미': ['독서', '영화감상', '코딩'], '주소': '서울시 강남구'}
df = pd.Series(person1)
# df = pd.DataFrame(person1)

df.to_json('person1.json', index=False)


person_data = pd.read_json('person1.json', orient='index')

values = person_data.values
for idx, data in enumerate(person_data.index):
    print(f"{data}: {values[idx][0]}")
