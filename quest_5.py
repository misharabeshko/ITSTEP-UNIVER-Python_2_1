medicines = [
    ("Амоксицилін", 150, "antibiotic", 18.5),
    ("Вітамін С", 300, "vitamin", 3.2),
    ("Вакцина БЦЖ", 50, "vaccine", 27.0),
    ("Анальгин", "багато", "vitamin", 20.0),
    ("Аспірин", 100, "painkiller", 15.0)
]

for item in medicines:
    name, quantity, category, temperature = item

    is_valid_qty = isinstance(quantity, int) and not isinstance(quantity, bool)
    is_valid_temp = isinstance(temperature, (float, int)) and not isinstance(temperature, bool)

    if not is_valid_qty or not is_valid_temp:
        print(f"Препарат: {name} - Помилка даних")
        continue


    if temperature < 5:
        temp_status = "Надто холодно"
    elif temperature > 25:
        temp_status = "Надто жарко"
    else:
        temp_status = "Норма"


    match category:
        case "antibiotic":
            cat_status = "Рецептурний препарат"
        case "vitamin":
            cat_status = "Вільний продаж"
        case "vaccine":
            cat_status = "Потребує спецзберігання"
        case _:
            cat_status = "Невідома категорія"


    print(f"Препарат: {name} | Категорія: {cat_status} | Температура: {temp_status}")


