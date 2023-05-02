#Desenvolva um programa em Python que calcule o IMC (índice de massa corpórea) de uma pessoa. Fórmula: (peso/altura²)
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
def imc(a,b):
    calc = a/(b**2)
    print(f"O seu IMC é {calc:.2f}")
imc(peso,altura)