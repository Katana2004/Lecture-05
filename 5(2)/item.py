import logging

logger = logging.getLogger(__name__)

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        logger.info(f"Создан объект MenuItem: {self.name} - {self.price}")