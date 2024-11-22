"""
Exiba a tabuada do 1 ao 10.
"""
n = 1

while n <= 10:
    multiplicador = 1
    print(f"\nTabuada do {n}")
    while multiplicador <= 10:
        print(f"{n} x {multiplicador} = {n * multiplicador}")
        multiplicador += 1
    n += 1