alice_in_wonderland = ''' 
"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.
\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.
\n"Oh, you\n're sure to do that," said the Cat, \n "if you only walk long enough." 
'''
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04

"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
square_black_sea = 436402
square_azov_sea = 37800
calculate_area = "Підрахувати загальну площу"
# find sum square of two seas
#solution:
calculate_area= square_black_sea + square_azov_sea
print("Загальна площа дорівнює", calculate_area)
# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
number_of_warehouses = 3
total_amount_of_goods = 375291
warehouse_1_plus_2 = 250449
warehouse_2_plus_3 = 222950
warehouse_1 = "Надрукувати, Скільки товарів у першому складі?"
warehouse_2 = "Надрукувати, Скільки товарів у другому складі?"
warehouse_3 = "Надрукувати, Скільки товарів у третьому складі?"
#solution
warehouse_1 = total_amount_of_goods - warehouse_2_plus_3
warehouse_3 = total_amount_of_goods - warehouse_1_plus_2
warehouse_2 = total_amount_of_goods - (warehouse_1 + warehouse_3)
sol_sum = warehouse_1 + warehouse_2 + warehouse_3

print("Warehous 1 have:", warehouse_1)
print("Warehous 2 have:", warehouse_2)
print("Warehous 3 have:", warehouse_3)
print("Recheck, counted sum = condition sum :", sol_sum == total_amount_of_goods  )
# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
credit_time = 18 #"Monnths"
mounthly_payment = 1179 #hrivnas
total_price = "Треба визначитити"
# solution #6
total_price = credit_time * mounthly_payment
print('Computer price = ', total_price)
# task 07

"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
numerator1 = 8019
divider1 = 8
remainder1 = numerator1 % divider1
print("Remainder =", remainder1)
numerator2 = 9907
divider2 = 9
remainder2 = numerator2 % divider2
print("Remainder =", remainder2)
numerator3 = 2789
divider3 = 5
remainder3 = numerator3 % divider3
print("Remainder =", remainder3)
numerator4 = 7248
divider4 = 6
remainder4 = numerator4 % divider4
print("Remainder =", remainder4)
numerator5 = 7128
divider5 = 5
remainder5 = numerator5 % divider5
print("Remainder =", remainder5)
numerator6 = 19224
divider6 = 9
remainder6 = numerator6 % divider6
print("Remainder =", remainder6)
# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

# Grocery list for Irinka's birthday:
list = [
    ("Піца велика", 4, 274),
    ("Піца середня", 2, 218),
    ("Сік", 4, 35),
    ("Торт", 1, 350),
    ("Вода", 3, 21)
]
total_price = ((list[0][1] * list[0][2]) + (list[1][1] * list[1][2]) + (list[2][1] * list[2][2]) +
               (list[3][1] * list[3][2]) + (list[4][1] * list[4][2]))
print(total_price)

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
total_photo_number = 232
amount_per_list = 8
total_amount_of_lists = 232/8
print(float(total_amount_of_lists))

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

trip_km = 1600
fuel_consumption = 9 # per 100 km
fuel_tank = 48
total_fuel = fuel_consumption * trip_km / 100
total_petrol_statio_visits = total_fuel / fuel_tank
print(total_fuel)
print(total_petrol_statio_visits)