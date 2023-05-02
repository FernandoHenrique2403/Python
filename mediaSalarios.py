#Calcular a média salarial do últimos seis salários recebidos, mostre no vídeo o resultado
contador = 0 
salario = 0
soma = 0
while(contador<6):
    contador+=1
    salario = float(input(f"Qual o {contador}° salario??"))
    soma = soma+salario
    media = soma/contador
    print(f"A média dos {contador} últimos salários é : R$ {media}")