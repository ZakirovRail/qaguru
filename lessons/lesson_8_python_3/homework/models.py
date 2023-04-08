from dataclasses import dataclass


@dataclass
class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        return self.quantity >= quantity

    def buy(self, quantity):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if self.check_quantity(quantity):
            self.quantity -= quantity
        else:
            raise ValueError(
                f"The requested amount of quantity: '{quantity}' higher that existing one:'{self.quantity}'")

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """
    #  Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    #  TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    # products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}
        # self.products: dict[Product, int] = {}

    def add_product(self, product: Product, quantity=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        self.products[product] = self.products.get(product, 0) + quantity

    def remove_product(self, product: Product, quantity=None):
        """
        Метод удаления продукта из корзины.
        Если quantity не передан, то удаляется вся позиция
        Если quantity больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if quantity is None or quantity >= self.products[product]:
            self.products.pop(product)
        else:
            self.products[product] -= quantity

    def clear(self):
        self.products = {}

    def get_total_price(self) -> float:
        total_price = sum([product.price * quantity for product, quantity in self.products.items()])
        return total_price

    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        for product, quantity in self.products.items():
            product.buy(quantity)
        self.clear()
