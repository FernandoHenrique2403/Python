#Desenvolva um programa em Python que solicite dois números ao usuário e, em seguida, realiza todas as operações aritméticas, mostrando o resultado na tela.
num1 = int(input("Digite o Primeiro número "))
num2 = int(input("Digite o Segundo número "))
def soma(a,b):
    som = a+b
    print(som)
def sub (a,b):
    sub = a-b
    print(sub)
def mult(a,b):
    mul=a*b
    print(mul)
def div(a,b):
    di=a/b
    print(di)
soma(num1,num2)
sub(num1,num2)
mult(num1,num2)
div(num1,num2)