list1 = list()
sum = 0

for i in range(0,101,3):
    if i != 0:
        list1.append(i)
        sum += i      

print(f'1부터 100까지 3의 배수: {list1}')
print(f'3의 배수의 합: {sum}')
print(f'3의 배수의 개수: {len(list1)}')