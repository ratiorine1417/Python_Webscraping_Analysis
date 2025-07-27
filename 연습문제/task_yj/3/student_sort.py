student_info = [{'name':'박민수', 'age':'21', 'major':'경영학과'},
                {'name':'최수진', 'age':'23', 'major':'수학과'},
                {'name':'김철수', 'age':'20', 'major':'컴퓨터공학과'},
                {'name':'이영희', 'age':'22', 'major':'영어영문학과'}]
student_age = []

print('나이 순으로 정렬된 학생 목록:')
# 1번째 풀이
# for student in student_info:
#     student_age.append((student['age'], (student['name']), (student['major'])))
# sorted_age = sorted(student_age)

# for age in sorted_age:
#     list1 = list(age)
#     print(f'{list1[1]} ({list1[0]}세) - {list1[2]}')

# 2번째 풀이
for idx, student in enumerate(student_info):
    student_age.append((student['age'], idx))
sorted_age = sorted(student_age)
first, second, third, forth = sorted_age
list1 = [first, second, third, forth]

for i in list1:
    agen, index = i
    stu = student_info[index]
    print(f'{stu['name']} ({stu['age']}세) - {stu['major']}')