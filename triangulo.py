#Desenvolva um programa em Python para inserir comprimento e largura de um triângulo e encontrar sua área. Fórmula: (base x altura)/2
base = float(input("Entre com a medida da base em cm "))
altura = float(input("Entre com a medida da altura em cm "))
def triangulo(a,b):
    area = (a*b)/2
    print(f"A área do triangulo é {area}cm²")
triangulo(base,altura)