def eval_atom(items):    
    token = items.pop(0)
    
    if token == '(':
        result = eval_add(items)
        
        if items and items[0] == ')':
            items.pop(0)
            
        return result 
    
    return float(token)


def eval_mul(items):
    left = eval_atom(items)
    
    while items and items[0] in ('*', '/'):
        op = items.pop(0)
        right = eval_atom(items)
        
        if op == '*':
            left = left * right
        elif op == '/':
            if right == 0:
                print("Помилка: ділення на нуль!")
                return 0
            left = left / right
            
    return left



def eval_add(items):
    left = eval_mul(items)
    
    while items and items[0] in ('+', '-'):
        op = items.pop(0)
        right = eval_mul(items)
        
        if op == '+':
            left = left + right
        elif op == '-':
            left = left - right
            
    return left



def calc(expr):
    for op in "+-*/()":
        expr = expr.replace(op, f" {op} ")
    
    items = expr.split()
    result = eval_add(items)
    
    return result




text = input("Введіть вираз: ")
res = calc(text)
print("Відповідь:", res)