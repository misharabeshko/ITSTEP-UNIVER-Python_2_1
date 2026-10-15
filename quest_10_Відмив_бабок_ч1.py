def shadow(limit: float = 200):
    def decorator(func):
        def wrapper():
            total_sum = 0.0
            limit_exceeded = False
            
            for item in func():
                print(item)
                
                parts = item.split()
                
                if len(parts) == 2:
                    try:
                        amount = float(parts[1])
                        total_sum += amount
                        
                        if total_sum > limit and not limit_exceeded:
                            print("Тіньовий ліміт перевищено. Активую схему.")
                            limit_exceeded = True
                    
                    except ValueError:
                        pass
                
                yield item
            
            return total_sum
        
        return wrapper
    
    return decorator



def suspicious_counter(threshold: float = 0):
    def decorator(func):
        def wrapper():
            suspicious_total = 0.0
            
            for item in func():
                parts = item.split()
                if len(parts) == 2:
                    try:
                        amount = float(parts[1])

                        if amount > threshold:
                            suspicious_total += amount
                            print(f"[Suspicious Counter] Увага! Знайдено велику транзакцію ({amount}). Загалом підозрілого: {suspicious_total}")
                    except ValueError:
                        pass
                
                yield item

            return suspicious_total
        
        return wrapper
    return decorator



@suspicious_counter(threshold=100)
@shadow(limit=200)
def generate_transactions():
    yield "payment 120"
    yield "refund 50"
    yield "transfer 300"
    yield "payment bad_string"
    yield "transfer 100"






print("---- ТЕСТ ----")
    

gen = generate_transactions()


try:
    while True:
        next(gen)
except StopIteration as e:
    final_sum = e.value
    # print(f"\nФінальна сума, повернута генератором: {final_sum}")


