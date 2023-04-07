"""
Протестируйте классы из модуля homework/models.py
"""
import pytest
from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


# @pytest.fixture(scope="function")
@pytest.fixture
def cart():
    cart = Cart()
    return cart


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        assert product.check_quantity(product.quantity)
        assert not product.check_quantity(product.quantity + 1)
        assert not product.check_quantity(5000), "Requested quantity of product is higher then exists in shop"
        assert product.check_quantity(1000)
        assert product.check_quantity(999)
        assert not product.check_quantity(1001), "Requested quantity of product is higher then exists in shop"

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(0)
        is_zero_quantity = product.quantity
        assert is_zero_quantity == 1000

        initial_quantity = product.quantity
        product.buy(100)
        left_quantity = product.quantity
        assert initial_quantity > left_quantity
        assert left_quantity == 900

        product.buy(899)
        is_last_quantity = product.quantity
        assert is_last_quantity == 1

        product.buy(1)
        is_zero_quantity = product.quantity
        assert is_zero_quantity == 0

        product.buy(0)
        is_zero_quantity = product.quantity
        assert is_zero_quantity == 0

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        # print(f"\n QUANTITY = {product.quantity}")
        # initial_quantity = product.quantity
        with pytest.raises(ValueError,
                           match="The requested amount of quantity: '1001' higher that existing one:'1000'"):
            product.buy(1001)

        with pytest.raises(ValueError,
                           match="The requested amount of quantity: '1050' higher that existing one:'1000'"):
            product.buy(1050)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_successful_add_product(self, product, cart):
        cart.add_product(product, quantity=5)
        assert cart.products[product] == 5, "Failed to add a product"

        cart.add_product(product, quantity=10)
        assert cart.products[product] == 15, "Failed to add a product"

    def test_successful_add_existing_product_to_cart(self, product, cart):
        cart.add_product(product, quantity=5)
        assert cart.products[product] == 5, "Failed to add a product"

        cart.add_product(product, quantity=5)
        assert cart.products[product] == 10, "Failed to add a product"

    def test_successful_remove_product(self, product, cart):
        cart.add_product(product, quantity=5)
        cart.remove_product(product)
        assert product not in cart.products

        cart.add_product(product, 1)
        cart.remove_product(product, 2000)
        assert product not in cart.products

        cart.add_product(product, 100)
        cart.remove_product(product, 100)
        assert product not in cart.products

        cart.add_product(product, 100)
        cart.remove_product(product, 40)
        assert cart.products == {product: 60}



    def test_successful_clear(self, product, cart):
        cart.add_product(product, quantity=5)
        cart.clear()
        assert product not in cart.products

    def test_get_total_price(self, product, cart):
        cart.add_product(product, 1)
        assert cart.get_total_price() == 100, 'Wrong total price'

        cart.add_product(product, 4)
        assert cart.get_total_price() == 500, 'Wrong total price'

    def test_successful_buy(self, product, cart):
        cart.add_product(product, quantity=100)
        cart.buy()
        assert product.quantity == 900, "Wrong quantity for left product"

        cart.add_product(product, quantity=100)
        cart.buy()
        assert product.quantity == 800, "Wrong quantity for left product"

        cart.add_product(product, quantity=800)
        cart.buy()
        assert product.quantity == 0, "Wrong quantity for left product"

    def test_buy_more_than_stock(self, product, cart):
        cart.add_product(product, product.quantity + 1)
        with pytest.raises(ValueError):
            cart.buy()
