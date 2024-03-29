import pytest
from src.classes import Category,Product

@ pytest.fixture()
def category_tv():
    return Category ("Телевизоры", "Описание телевизоров", ["Самсунг","Тошиба", "Филипс"])
@ pytest.fixture()
def product_model():
    return Product ("Sony_1", "Описание модели Sony", 25000, 18)


def test_init_category(category_tv):
    assert category_tv.name =="Телевизоры"
    assert category_tv.description == "Описание телевизоров"
    assert category_tv.products == ["Самсунг","Тошиба", "Филипс"]
    assert category_tv.number_of_categories ==1
    assert category_tv.quantity_prodacts ==3


def test_init_product(product_model):
    assert product_model.name =="Sony_1"
    assert product_model.description == "Описание модели Sony"
    assert product_model.price == 25000
    assert product_model.quantity == 18
