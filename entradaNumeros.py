#Faça um programa que solicite 2 números e informe:
#A soma dos Numeros
#O produto do Pirmeiro número pelo segundo
#O quadrado do primeiro número
#a Subtração do segundo número pelo primeiro


num1 = float(input("Digite o Primeiro número: "))
num2 = float(input("Digite o Segundo número: "))
def soma(a,b):
    som = a+b
    print(som)
def produto(a,b):
    prod = a*b
    print(prod)
def quadrado(a):
    quad = a**2
    print(quad)
def sub(a,b):
    sub = a-b
    print(sub)

soma(num1,num2)
produto(num1,num2)
quadrado(num1)
sub(num1,num2)