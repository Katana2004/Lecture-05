import logging
from menu import Menu

logger = logging.getLogger(__name__)

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