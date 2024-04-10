from src.classes import Category,Product

ex_1= Product ("Sony", "Описание Sony", 25000, 18)
ex_2= Product ("Samsung", "Описание Samsung", 35000, 8)

category_tv = Category ("Телевизоры", "Описание телевизоров",[ex_1,ex_2,ex_1])
category_smart = Category ("Телефоны", "Описание телефонов",[ex_1,ex_2])
print (category_tv.name)
print (category_tv.products.__repr__())
print (Category.all_quantity_category)
print (Category.all_quantity_unique_product)

