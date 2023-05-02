#Desenvolva um programa em Python para inserir comprimento e largura de um retângulo e encontre sua área. Fórmula: base x altura
alt = float(input("Entre com a altura em cm "))
base = float(input("Entre com o base em cm "))
def retangulo(a,b):
    area = a*b
    print(f"A área do Retângulo é {area}cm²")

retangulo(alt,base)