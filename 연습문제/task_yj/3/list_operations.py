import copy

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = copy.deepcopy(list1)

print(f'리스트1: {list1}')
print(f'리스트2: {list2}')
list3.extend(list2)
print(f'병합된 리스트: {set(list3)}')
set1 = set(list1)
set2 = set(list2)
print(f'공통 요소: {set1 & set2}')