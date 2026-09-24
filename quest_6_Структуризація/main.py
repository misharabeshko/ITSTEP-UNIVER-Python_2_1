from models import Antibiotic, Vitamin, Vaccine

medicines = [
    Antibiotic("Амоксицилін", 10, 45.5),
    Vitamin("Вітамін С", 50, 12.0),
    Vaccine("БЦЖ", 5, 200.0)
]

for med in medicines:
    print(med.info())

