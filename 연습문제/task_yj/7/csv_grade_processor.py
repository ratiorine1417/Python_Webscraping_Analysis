import pandas as pd

grade = {'name': ['김철수', '이영희', '박민수', '최수진'],
         'grade': [85, 92, 78, 95]}
df = pd.DataFrame(grade)

df.to_csv('grade.csv', index=False)

data_grade = pd.read_csv('grade.csv')

sum = 0
students = list(data_grade['name'])
score_list = list(data_grade['grade'])

print('성적 분석 결과:')
for i, student in enumerate(students):
    print(f'{student}: {score_list[i]}점')
    sum += score_list[i]
print(f'전체 평균: {sum/len(students)}점')