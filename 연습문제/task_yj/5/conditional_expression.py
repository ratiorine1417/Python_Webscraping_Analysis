score = 85
age = 17
max_or_min = 'max'
list1 = [2, 34, 42, 23, 12]
list2 = [5, -12, -8, 23]
list3 = list()

print(f'점수: {score}, 결과: 합격') if score > 80 else print(f'점수: {score}, 결과: 불합격')
print(f'나이: {age}, 상태: 미성년자') if age < 20 else print(f'나이: {age}, 상태: 성인')
print(f'숫자들의 최대값: {max(list1)}') if max_or_min == 'max' else print(f'숫자들의 최소값: {min(list1)}')
for num in list2:
    list3.append(num) if num > 0 else list3.append(abs(num))
print(f'양수들: {list3}')