def discounted(price, discount, max_discount=30, phone_name=""):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError("Слишком большая максимальная скидка")
    if discount >= max_discount:
        return price
    elif "iphone" in phone_name.lower() or not phone_name:
        return price
    else:
        return price - (price * discount / 100)
new_price = discounted(10000, 10, phone_name = 'sumsung')
print(new_price)