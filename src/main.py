from src.classes import Category,Product,Smartphone,Lawn_grass

ex_1= Product ("Sony", "Описание Sony", 25000, 18, "белый")
ex_2= Smartphone ("Samsung", "Описание Samsung", 35000, 8,"черный",2,"S9", 156)
ex_3= Product ("Miele", "Описание Miele", 18000, 88,"черный")

category_tv = Category ("Телевизоры", "Описание телевизоров",[ex_1,ex_2,ex_1])
category_smart = Category ("Телефоны", "Описание телефонов",[ex_1,ex_2])
print (category_tv.name)
print (Category.all_quantity_category)
print (Category.all_quantity_unique_product)

new_prod= Product.create_product("Miele", "Описание Miele",18000,88,"черный")
new_prod.get_price =50000

print (new_prod)

category_tv.add_products(ex_3)

new= category_tv.list_products
print (new)

print(category_tv)

print (ex_1 + ex_3)

print (len(category_smart))

print (repr(ex_2))

new1=Smartphone.create_product("Miele", "Описание Miele",18000,88,"черный",128, "e34", 256)
print (new1)

new2=Lawn_grass.create_product("Miele", "Описание Miele",18000,9,"черный", "germany", 2023)
print (new2)

new3= category_tv.average_sum
print (new3)