price = int(input('상품 가격을 입력하세요: '))
discount = int(input('할인율을 입력하세요(%): '))

print(f'원래 가격: {price}원')
print(f'할인율: {discount}%')
print(f'할인 금액: {price*discount/100}원')
print(f'최종 가격: {price*(100-discount)/100}원')
