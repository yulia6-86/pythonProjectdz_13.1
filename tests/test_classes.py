import pytest
from src.classes import Category
from src.classes import Product
from src.classes import Smartphone


@ pytest.fixture()
def product_ex():
    return Product ("Sony", "Описание Sony", 25000, 18, "черный")
@ pytest.fixture()
def product_ex_2():
    return Product ("Samsung", "Описание Samsung", 35000, 8, "белый")
@ pytest.fixture()
def product_ex_3():
    return Product ("Miele", "Описание Miele", 18000, 88, "черный")
@ pytest.fixture()
def product_ex_4():
    return Smartphone ("Miele", "Описание Miele", 18000, 88, "черный",2,"S9", 156)
@ pytest.fixture()
def category_tv():
    return Category ("Телевизоры", "Описание телевизоров",[Product ("Sony", "Описание Sony", 25000, 18, "черный"), Product ("Samsung", "Описание Samsung", 35000, 8, "белый")])

def test_init_category(category_tv):
    assert category_tv.name =="Телевизоры"
    assert category_tv.description == "Описание телевизоров"
    assert Category.all_quantity_category ==1
    assert Category.all_quantity_unique_product ==2


def test_init_product(product_ex):
    assert product_ex.name =="Sony"
    assert product_ex.description =="Описание Sony"
    assert product_ex.price == 25000
    assert product_ex.quantity == 18

def test_product_category(category_tv):
    assert category_tv.list_products  == ['Sony, 25000 руб. Остаток: 18 шт.',
                                     'Samsung, 35000 руб. Остаток: 8 шт.',
                                     ]


def test_get_price(product_ex_3):
    assert product_ex_3.get_price == 18000
    product_ex_3.get_price = 185000
    assert product_ex_3.get_price == 185000


def test_str_category(category_tv):
    assert category_tv.__str__() == "Название категории Телевизоры, количество продуктов: 26 шт."


def test_add_prodact(product_ex, product_ex_2):
    assert product_ex + product_ex_2 == 730000


def test_add_product(product_ex, product_ex_4):
    with pytest.raises(TypeError):
         assert product_ex.__add__(product_ex_4) == 2034000



def test_len_prodact(category_tv):
    assert len (category_tv) == 26


