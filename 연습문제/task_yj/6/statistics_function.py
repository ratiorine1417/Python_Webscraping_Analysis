import numpy as np

list1 = [10, 20, 30, 40, 50]

print(f'숫자들: {list1}')
print(f'평균: {sum(list1)/len(list1)}') # np.mean(list1)
print(f'최댓값: {max(list1)}')
print(f'최솟값: {min(list1)}')
print(f'표준편차: {np.std(list1, ddof=1):.2f}') # ddof=1은 표본 표준 편차/분모는 데이터 개수에서 1을 뺀 값(N-1)
# ddof=0(모집단의 표준 편차/분모는 데이터의 개수(N))이 default