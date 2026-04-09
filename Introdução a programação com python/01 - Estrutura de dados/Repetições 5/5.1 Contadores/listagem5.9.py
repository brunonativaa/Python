# Tabuada simples

n = float(input("Tabuada de:"))

x = 1 

while x <= 10:
    rest = n / x
    print(f"{n} x {x} = {rest:.2f} ")
    x = x + 1
