def calc():
    a = float(input("First number: "))
    op = input("Operation (+ - * /): ").strip()
    b = float(input("Second number: "))
    if op == '+':  res = a + b
    elif op == '-': res = a - b
    elif op == '*': res = a * b
    elif op == '/': res = a / b
    else: raise ValueError("Unknown operator")
    print(f"Result: {res}")

if _name_ == "_main_":
    calc()