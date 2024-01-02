import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        logger.info(f"Создан объект MenuItem: {self.name} - {self.price}")

class Menu:
    def __init__(self):
        self.menu_items = []
        logger.info("Создан объект Menu")

    def add_item(self, name, price):
        item = MenuItem(name, price)
        self.menu_items.append(item)
        logger.info(f"Добавлено блюдо в меню: {item.name} - {item.price}")

class Order:
    def __init__(self, client_name, menu):
        self.client_name = client_name
        self.menu = menu
        self.items = []
        logger.info(f"Создан объект Order для клиента: {self.client_name}")

    def add_item(self, item_name):
        for menu_item in self.menu.menu_items:
            if menu_item.name == item_name:
                self.items.append(menu_item)
                logger.info(f"Добавлено блюдо в заказ {self.client_name}: {item_name}")
                return
        logger.warning(f"Блюдо {item_name} не найдено в меню")

    def calculate_total_price(self):
        total_price = sum(item.price for item in self.items)
        logger.info(f"Рассчитана общая стоимость заказа {self.client_name}: {total_price}")
        return total_price

menu = Menu()
menu.add_item("Пицца", 10)
menu.add_item("Салат", 5)

order = Order("Иван", menu)
order.add_item("Пицца")
order.add_item("Суп")
total_price = order.calculate_total_price()

print(f"Итоговая стоимость заказа: {total_price}")