from abc import ABC, abstractmethod


class AbstractProduct (ABC):

    @abstractmethod
    def create_product(self, value):
        """
        Функция для инициализации нового объекта
        """
        pass


class MixinRepr:

    def __init__(self, *args, **kwargs):
        """
        Функция печатает информацию какой объект был создан и с какими свойствами
        """
        print(repr(self))

    def __repr__(self):
        """
        Функция возвращает строковое отображение объекта при его создании
        """
        return f"{self.__class__.__name__}({self.__dict__})"


class Category:
    """Создаем класс категорий с атрибутами имя, описание,товары"""

    name: str
    description: str
    products: []
    all_quantity_category = 0
    all_quantity_unique_product = 0

    def __init__ (self,name,description,products=[]):
        self.name=name
        self.description=description
        self.__products=products
        Category.all_quantity_category += 1  # Подсчитывает категории товаров
        Category.all_quantity_unique_product += len(set(self.__products))  # Подсчитывает уникальные продукты

    def add_products(self,value):
        """Добавление товаров в cписок только объекты Product или его наследников"""

        if not isinstance(value, Product):
            raise TypeError
        elif value.quantity == 0:
            raise ValueError #Продукт с нулевым количеством не может быть добавлен
        self.__products.append(value)


    @property
    def list_products(self):
        """Выводим товары в определенном формате """
        output = []
        for product in self.__products:
            output.append (f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.')
        return output

    def __repr__(self):
        return f"{self.__class__.__name__} ({self.name} {self.description} {self.__products})"

    def __len__(self):
        """ Подсчёт кол-ва продуктов в категории. """
        product_counter = 0
        for product in self.__products:
            product_counter += product.quantity
        return product_counter

    def __str__(self):
        """ Вывод кол-ва продуктов в следующем виде: 'Название категории, количество продуктов: 200 шт.' """
        return f"Название категории {self.name}, количество продуктов: {self.__len__()} шт."

    def average_sum(self):
        """
        Метод, который подсчитывает средний ценник всех товаров.
        Если в Категории нет  ни одного товар, возвращает 0
        """
        try:
            total_sum = 0
            for product in self.__products:
                total_sum += product.price
            average_sum = total_sum / len(self.__products)
            return average_sum
        except ZeroDivisionError:
            return 0


class Product (MixinRepr, AbstractProduct):
    "Создаем класс продуктов с атрибутами имя,описание,цена,количество"
    name: str
    description: str
    price: float
    quantity: int
    color = str

    def __init__(self,name,description,price,quantity, color):
        self.name=name
        self.description=description
        self.price=price
        self.quantity=quantity
        self.color = color
        super().__init__()

    def __str__(self):
        """ Вывод списка продуктов в определенном виде"""
        return f"{self.name}, {self.price} руб Остаток: {self.quantity} шт."

    @classmethod
    def create_product(cls, name, description, price, quantity, color):
        return cls(name,description,price,quantity, color)

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

    def __add__(self, other):
        """Магический метод add для возможности сложения экземпляров Класса Складывать можно только объекты
        из одинаковых категорий"""
        if type(other) is not type(self):
            raise TypeError
        return self.quantity * self.price + other.quantity * other.price


class Smartphone(Product):
    productivity = int  # Производительность
    model = str  # Модель
    memory = int  # Емкость внутренней памяти

    def __init__(self, name, description, price, quantity, color, productivity,model, memory):
        super().__init__(name, description, price, quantity,color)
        self.productivity = productivity
        self.model = model
        self.memory = memory

    @classmethod
    def create_product(cls, name, description, price, quantity, color, productivity, model, memory):
        return cls(name, description, price, quantity, color, productivity,model, memory)


class Lawn_grass(Product):
    def __init__(self, name, description, price, quantity, color, country, period):
        super().__init__(name, description, price, quantity, color)
        self.country = country
        self.period = period

    @classmethod
    def create_product(cls, name, description, price, quantity, color, country, period):
        return cls(name, description, price, quantity, color, country, period)







