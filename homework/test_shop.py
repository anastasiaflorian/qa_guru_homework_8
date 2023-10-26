"""
Протестируйте классы из модуля homework/models.py
"""
import pytest
from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture()
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        is_correct_product_quantity = 1 <= product.quantity <= 1000
        assert is_correct_product_quantity == True

    def test_product_buy(self, product):
        # Купить доступное количество продуктов
        product.buy(5)
        assert product.quantity == 995

    def test_product_buy_more_than_available(self, product):
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, product, cart):
        # добавить в пустую корзину
        cart.add_product(product, 1)
        assert cart.products[product] == 1
        # добавьте тот же товар в корзину
        cart.add_product(product, 1)
        assert cart.products[product] == 2

    def test_remove_product(self, product: Product, cart):
        # добавить и удалить одинаковое количество продуктов
        cart.add_product(product, 10)
        cart.remove_product(product, 10)
        assert not cart.products
        # добавить и удалить разное количество продуктов
        cart.add_product(product, 25)
        cart.remove_product(product, 20)
        assert cart.products[product] == 5

    def test_clear(self, cart, product):
        cart.add_product(product, 50)
        cart.clear()
        assert not cart.products

    def test_buy(self, cart, product):
        cart.add_product(product, 999)
        cart.buy()
        quantity_products = product.quantity == 1
        assert quantity_products == 1
        cart.add_product(product, 1001)
        with pytest.raises(ValueError):
            cart.buy()