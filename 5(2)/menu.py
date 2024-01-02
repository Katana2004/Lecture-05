import logging
from item import MenuItem

logger = logging.getLogger(__name__)

class Menu:
    def __init__(self):
        self.menu_items = []
        logger.info("Создан объект Menu")

    def add_item(self, name, price):
        item = MenuItem(name, price)
        self.menu_items.append(item)
        logger.info(f"Добавлено блюдо в меню: {item.name} - {item.price}")