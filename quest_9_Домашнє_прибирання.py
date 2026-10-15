from abc import ABC, abstractmethod


class JunkItem:

    def __init__(self, name: str, quantity: int, value: float):
        self.name = name
        self.quantity = quantity
        self.value = value

    def __repr__(self):
        return f"JunkItem(name='{self.name}', quantity={self.quantity}, value={self.value})"



class StorageBackend(ABC):

    @abstractmethod
    def save(self, items: list[JunkItem]) -> None:
        pass

    @abstractmethod
    def load(self) -> list[JunkItem]:
        pass



class FileJunkStorage(StorageBackend):

    def __init__(self, filename: str):
        self.filename = filename

    def serialize(self, items: list[JunkItem]) -> None:
        with open(self.filename, "w", encoding="utf-8") as f:
            for item in items:
                value_str = str(item.value).replace(".", ",")
                line = f"{item.name}|{item.quantity}|{value_str}\n"
                f.write(line)

    def parse(self, filename: str = None) -> list[JunkItem]:
        target_file = filename if filename else self.filename
        items = []

        try:
            with open(target_file, "r", encoding="utf-8") as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    
                    if not line:
                        continue

                    parts = line.split("|")


                    if len(parts) != 3:
                        print(
                            f"[Попередження] Рядок {line_num} пропущено: очікувалося 3 поля, знайдено {len(parts)}."
                        )
                        continue

                    name, qty_str, val_str = parts


                    try:
                        quantity = int(qty_str)
                    except ValueError:
                        print(
                            f"[Попередження] Рядок {line_num} пропущено: кількість '{qty_str}' не є цілим числом."
                        )
                        continue


                    try:
                        value = float(val_str.replace(",", "."))
                    except ValueError:
                        print(
                            f"[Попередження] Рядок {line_num} пропущено: ціна '{val_str}' не є числом з плаваючою комою."
                        )
                        continue

                    items.append(JunkItem(name, quantity, value))

        except FileNotFoundError:
            print(f"[Попередження] Файл {target_file} не знайдено.")



        return items


    def save(self, items: list[JunkItem]) -> None:
        self.serialize(items)

    def load(self) -> list[JunkItem]:
        return self.parse()



class JunkWarehouse:

    def __init__(self, storage: StorageBackend):
        self.storage = storage
        self.items: list[JunkItem] = []

    def add_item(self, item: JunkItem) -> None:
        self.items.append(item)

    def save_stock(self) -> None:
        self.storage.save(self.items)

    def load_stock(self) -> None:
        self.items = self.storage.load()

    def show_items(self) -> None:
        for item in self.items:
            print(item)




print("--- 1. Створення складу та предметів ---")
file_storage = FileJunkStorage("warehouse.csv")
warehouse = JunkWarehouse(file_storage)

warehouse.add_item(JunkItem("Бляшанка", 5, 2.5))
warehouse.add_item(JunkItem("Стара плата", 3, 7.8))
warehouse.add_item(JunkItem("Купка дротів", 10, 1.2))

print("Початкові предмети на складі:")
warehouse.show_items()



print("\n--- 2. Запис у файл ---")
warehouse.save_stock()
print("Дані успішно записано у 'warehouse.csv'.")



print("\n--- 3. Читання з файлу та перевірка ---")
new_warehouse = JunkWarehouse(file_storage)
new_warehouse.load_stock()

print("Предмети після зчитання з файлу:")
new_warehouse.show_items()



# Тестування зіпсованих рядків
print("\n--- 4. Тестування зіпсованих рядків ---")
with open("warehouse.csv", "w", encoding="utf-8") as f:
    f.write("Бляшанка|5|2,5\n")
    f.write("Зіпсований рядок без палок\n")
    f.write("Трансформатор|не_число|5,0\n")
    f.write("Старий корпус|2|не_флоат\n")
    f.write("Шурупи|100|0,5\n")

print("Запуск зчитування з обробкою помилок:")
validated_storage = FileJunkStorage("warehouse.csv")
recovered_items = validated_storage.parse()


print("\nУспішно відновлені коректні предмети:")
for item in recovered_items:
    print(item)


