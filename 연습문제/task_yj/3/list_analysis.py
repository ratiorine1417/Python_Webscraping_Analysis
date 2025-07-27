list1 = [15, 3, 27, 8, 19, 12, 31]

print(f'숫자 목록: {list1}')
print(f'최댓값: {max(list1)}')
print(f'최솟값: {min(list1)}')
list1.remove(max(list1))
print(f'두 번째로 큰 값: {max(list1)}')