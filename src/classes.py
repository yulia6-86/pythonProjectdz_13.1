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
        self.__products=products
        Category.all_quantity_category += 1  # Подсчитывает категории товаров
        Category.all_quantity_unique_product += len(set(self.__products))  # Подсчитывает уникальные продукты


    def add_products(self, value):
        """Добавление товаров в cписок """
        self.__products.append(value)


    @property
    def list_products(self):
        """Выводим товары в определенном формате """
        output = []
        for product in self.__products:
            output.append (f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.')
        return output


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

    @classmethod
    def create_product(cls,name,description,price,quantity):
        return cls (name,description,price,quantity)

    @property
    def get_price(self):
        """
        Геттер для свойства цены
        """
        return self.price

    @get_price.setter
    def get_price(self, value: float):
        """
        Сеттер для свойства цены, устанавливает новое значение если оно больше 0
        """
        if value <= 0:
            print("цена введена некорректная")
        elif value < self.price:
            while True:
                answer = input("Вы уверены что хотите понизить цену: (y/n)").lower()
                if answer == "y":
                    self.price = value
                    break

                elif answer == "n":
                    self.price = self.price
                    break

        else:
            self.price = value



