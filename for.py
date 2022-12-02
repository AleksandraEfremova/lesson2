sales = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def sum_sold(phone_sold):
    sales_sum = 0
    for sales in phone_sold:
        sales_sum +=sales
    return sales_sum
    

total_sales_sum = 0
for one_sale in sales:
    phone_sales_sum = sum_sold(one_sale['items_sold'])
    print(f"Cуммарное количество продаж {one_sale['product']}: {phone_sales_sum}")
    total_sales_sum += phone_sales_sum

print(f'Суммарное количество всех продаж: {total_sales_sum}')


def avg_sold(phone_sold):
    sales_sum = 0
    for sales in phone_sold:
        sales_sum += sales
        sales_avg = sales_sum / len(phone_sold)
    return sales_avg

total_sales_sum = 0
for one_sale in sales:
    phone_sales_avg = avg_sold(one_sale['items_sold'])
    print(f"Среднее количество продаж {one_sale['product']}: {phone_sales_avg}")
    total_sales_sum += phone_sales_sum

print(f'Среднее количество продаж всех товаров: {total_sales_sum / len(sales)}')




