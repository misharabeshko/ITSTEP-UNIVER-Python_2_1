def process_deals(deals):
    processed_deals = []

    for name, amount, status in deals:
        if not isinstance(amount, (int, float)):
            amount_category = "Фальшиві дані"
        else:
            if amount < 100:
                amount_category = "Дрібнота"
            elif 100 <= amount <= 999:
                amount_category = "Середнячок"
            else:
                amount_category = "Великий клієнт"

        match status:
            case "clean":
                decision = "Працювати без питань"
            case "suspicious":
                decision = "Перевірити документи"
            case "fraud":
                decision = "У чорний список"
            case _:
                decision = "Невідомий статус"

        processed_deals.append((name, amount_category, decision))

    return processed_deals



deals_list = [
    ("Олександр", 75.50, "clean"),
    ("Марія", 500, "suspicious"),
    ("Іван", 1500.00, "fraud"),
    ("Петро", "багато", "clean"),
    ("Анна", 250, "unknown_status")
]

result = process_deals(deals_list)

for client in result:
    print(f"Клієнт: {client[0]} \t|\t Сума: {client[1]} \t|\t Рішення: {client[2]}")