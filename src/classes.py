class Category:
    """Создаем класс категорий с атрибутами имя, описание,товары"""

    name: str
    description: str
    products: []
    all_quantity_category = 0
    all_quantity_unique_product = 0


    def __init__(self,name,description,products=[]):
        self.name=name
        self.description=description
        self.products=products
        Category.all_quantity_category += 1  # Подсчитывает категории товаров
        Category.all_quantity_unique_product += len(set(self.products))  # Подсчитывает уникальные продукты
        self.categories_count = Category.all_quantity_category
        self.product_count = Category.all_quantity_unique_product




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


    def __repr__(self):
        return f"'{self.name}', '{self.description}', {self.price}, {self.quantity}"



