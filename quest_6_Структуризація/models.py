from abc import ABC, abstractmethod

class Medicine(ABC):
    def __init__(self, name: str, quantity: int, price: float) -> None:
        if not isinstance(name, str):
            raise TypeError("Назва має бути рядком")
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise TypeError("Кількість має бути цілим числом")
        if not isinstance(price, (int, float)) or isinstance(price, bool):
            raise TypeError("Ціна має бути числом")
            
        self.name: str = name
        self.quantity: int = quantity
        self.price: float = float(price)

    @abstractmethod
    def requires_prescription(self) -> bool:
        pass

    @abstractmethod
    def storage_requirements(self) -> str:
        pass

    def total_price(self) -> float:
        return self.quantity * self.price

    @abstractmethod
    def info(self) -> str:
        pass


class Antibiotic(Medicine):
    def requires_prescription(self) -> bool:
        return True

    def storage_requirements(self) -> str:
        return "8–15°C, темне місце"

    def info(self) -> str:
        prescription = "Рецептурний" if self.requires_prescription() else "Вільний продаж"
        return f"Антибіотик: {self.name} | Кількість: {self.quantity} | Ціна: {self.total_price()} | {prescription} | Зберігання: {self.storage_requirements()}"


class Vitamin(Medicine):
    def requires_prescription(self) -> bool:
        return False

    def storage_requirements(self) -> str:
        return "15–25°C, сухо"

    def info(self) -> str:
        prescription = "Рецептурний" if self.requires_prescription() else "Вільний продаж"
        return f"Вітамін: {self.name} | Кількість: {self.quantity} | Ціна: {self.total_price()} | {prescription} | Зберігання: {self.storage_requirements()}"


class Vaccine(Medicine):
    def requires_prescription(self) -> bool:
        return True

    def storage_requirements(self) -> str:
        return "2–8°C, холодильник"

    def total_price(self) -> float:
        base_price = super().total_price()
        return base_price * 1.1

    def info(self) -> str:
        prescription = "Рецептурний" if self.requires_prescription() else "Вільний продаж"
        return f"Вакцина: {self.name} | Кількість: {self.quantity} | Ціна з націнкою: {self.total_price()} | {prescription} | Зберігання: {self.storage_requirements()}"

