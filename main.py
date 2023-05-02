a = int(input("Digite o valor do lado: "))
b = int(input("Digite o valor do lado: "))
c = int(input("Digite o valor do lado: "))

triangulo = True

if a + b <= c or a + c <= b or b + c <= a:
    print("Não é um triângulo")
    triangulo = False

if triangulo == True:
    if a == b and b == c:
        print("Equilátero")
    elif a == b or b == c or a == c:
        print("Isósceles")
    else:
        print("Escaleno")