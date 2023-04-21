a = int(input("digite o valor do lado:\n"))
b = int(input("digite o valor do lado:\n"))
c = int(input("digite o valor do lado:\n"))
if a == b and b == c:
    print("Equilátero")
if a == b and b != c:
    print("Isósceles")
elif a == c and c != b:
    print("Isósceles")
elif b == c and c != a:
    print("Isósceles")
elif b != c and c != a:
    print("Escaleno")