"""
Exiba a tabuada do 1 ao 10.
"""
for i in range (1, 11):
    print(f"\nTabuada do {i}")
    for multiplicador in range (1, 11):
        print(f"{i} x {multiplicador} = {i * multiplicador}")