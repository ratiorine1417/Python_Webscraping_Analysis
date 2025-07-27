stu_grade = {'김철수': 85, '이영희': 92, '박민수': 78, '최수진': 95}
sum_grade = 0

print('학생 성적:')
for stu, grade in stu_grade.items():
   print(f'{stu}: {grade}점')
   sum_grade += grade
print(f'평균 점수: {sum_grade/len(stu_grade)}점')
