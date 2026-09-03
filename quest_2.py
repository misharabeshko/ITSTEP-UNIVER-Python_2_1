def calculator():
    num1 = float(input("Введіть перше число: "))
    operator = input("Введіть операцію (+, -, *, /): ")
    num2 = float(input("Введіть друге число: "))

    match operator:
        case '+':
            result = num1 + num2
            print(f"Результат: {num1} + {num2} = {result}")

        case '-':
            result = num1 - num2
            print(f"Результат: {num1} - {num2} = {result}")

        case '*':
            result = num1 * num2
            print(f"Результат: {num1} * {num2} = {result}")

        case '/':
            if num2 != 0:
                result = num1 / num2
                print(f"Результат: {num1} / {num2} = {result}")
            else:
                print("Помилка: ділення на нуль неможливе!")

        case _:
            print("Помилка: невідома операція!")

calculator()