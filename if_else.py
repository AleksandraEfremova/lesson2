price=1000
balance=200
in_stock=0

print(bool(balance > price))
print(bool(in_stock))

if balance > price and in_stock:
    print('Одобряем оплату покупки')
elif not in_stock:
    print('Товара нет в наличии')
else:
    print('Пожалуйста, пополните баланс!')