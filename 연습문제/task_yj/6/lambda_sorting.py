list1 = [('김철수', 85), ('이영희', 92), ('박민수', 78), ('최수진', 95)]

print(f'학생 정보: {list1}')
list1.sort(key=lambda x: x[0])
print(f'이름순 정렬: {list1}')
list1.sort(key=lambda x: x[1])
print(f'점수순 정렬: {list1}')
list1.sort(key=lambda x: x[1], reverse=True)
print(f'점수 내림차순: {list1}')