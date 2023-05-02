#1) Escreva um programa que pergunte o nome do usuário. Guarde este nome em uma variável.
#2) Escreva um programa que dê boas-vindas a este usuário (valor da variável do exercício anterior).
#3) Escreva um programa que pergunte ao usuário anterior quantos copos de água ele bebeu hoje. Guarde a quantidade de copos de água em uma variável.
#4) Escreva um programa que mostre na tela o nome do usuário e aquantidade de águas que ele bebeu.

nome = input("Qual o seu nome? ")
print(f"Boas vindas {nome}")
copos = int(input(f"{nome}, quantos copos de água você bebeu hoje? "))
print(f"Usuário {nome} bebeu {copos} de água hoje!")