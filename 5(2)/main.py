import logging
from restaurant import Menu, Order

logging.basicConfig(level=logging.INFO)

menu = Menu()
menu.add_item("Пицца", 10)
menu.add_item("Салат", 5)

order = Order("Иван", menu)
order.add_item("Пицца")
order.add_item("Суп")
total_price = order.calculate_total_price()

print(f"Итоговая стоимость заказа: {total_price}")