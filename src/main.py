from src.classes import Category,Product

ex_1= Product ("Sony", "Описание Sony", 25000, 18)
ex_2= Product ("Samsung", "Описание Samsung", 35000, 8)
ex_3= Product ("Miele", "Описание Miele", 18000, 88)

category_tv = Category ("Телевизоры", "Описание телевизоров",[ex_1,ex_2,ex_1])
category_smart = Category ("Телефоны", "Описание телефонов",[ex_1,ex_2])
print (category_tv.name)
print (Category.all_quantity_category)
print (Category.all_quantity_unique_product)

new_prod= Product.create_product("Miele", "Описание Miele",18000,88)
new_prod.get_price =50000

print (new_prod)

category_tv.add_products(ex_3)

new= category_tv.list_products
print (new)

print(category_tv)

print (ex_1 + ex_2)