shopping_price = {'사과': 1000, '바나나': 800, '오렌지': 1500}
shopping_cart = {}
shopping_cart['사과'] = 2
shopping_cart['바나나'] = 3
shopping_cart['오렌지'] = 1
price = 0

print('쇼핑 카트:')
for key in shopping_cart.keys():
    price += shopping_cart[key]*shopping_price[key]
    print(f'{key}: {shopping_cart[key]}개 (개당 {shopping_price[key]}원) = {shopping_cart[key]*shopping_price[key]}원')
print(f'총 가격: {price}원')

