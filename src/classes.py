class Category:
    """Создаем класс категорий с атрибутами имя, описание,товары"""
    number_of_categories = 0
    name: str
    description: str
    products: []
    quantity_prodacts: int

    def __init__(self,name,description,products=[]):
        self.name=name
        self.description=description
        self.products=products
        self.number_of_categories += 1
        self.quantity_prodacts= len(self.products)

class Product:
    "Создаем класс продуктов с атрибутами имя,описание,цена,количество"
    name: str
    description: str
    price: float
    quantity: int


    def __init__(self,name,description,price,quantity):
        self.name=name
        self.description=description
        self.price=price
        self.quantity=quantity
