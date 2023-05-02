#Entrar com base e altura de um retângulo e calcular suas areas, mostrando na tela os resultados
baseT =float(input("Entre com a base do Triangulo "))
alturaT = float(input("Entre com a altura do Triangulo "))
baseR = float(input("Entre com a base do Retangulo"))
alturaR = float(input("Entre com a altura do Retangulo"))
def triangulo(a,b):
    area = (a*b)/2
    print(f"A área do triangulo é {area}cm²")
def retangulo(a,b):
    area = a*b
    print(f"A área do Retângulo é {area}cm²")

retangulo(alturaR,baseR)
triangulo(alturaT,baseT)