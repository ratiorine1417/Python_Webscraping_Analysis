def args_sum(x, y, list1, *args, **kwargs):
    sum = 0
    print(f"좌표: x={x}, y={y}")
    a, b, c = list1
    print(f'리스트 언패킹: a={a}, b={b}, c={c}')
    for arg in args:
        sum += arg
    print(f"가변 인수의 합: {sum}")
    keys = list(kwargs.keys())
    values = list(kwargs.values())
    print(f'키워드 인수들: {keys[0]}={values[0]}, {keys[1]}={values[1]}, {keys[2]}={values[2]}')
    

list1 = [1, 2, 3] # 리스트 언패킹
args_sum(10, 20, list1, 15, 20, 25, name='김철수', age=25, city='서울')