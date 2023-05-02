import random 


print("*******************************")
print("**--** Bem Vindo ao Jogo **--**")
print("*******************************")
print("\n")

numero_CPU = round(random.randrange(1,101))
print(numero_CPU)
chance = 3

while(chance>0):
    chute = int(input("Digite o Numero do seu Chute : "))
    print("Você digitou : ",chute)

    acertou = numero_CPU == chute
    maior = chute > numero_CPU
    menor = chute < numero_CPU
    if(acertou):
        print("Você Acertou !!")
        print("\nFIM DO JOGO!!!")
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi MAIOR que o numero da CPU")
            chance = chance -1
            print(f"Voce tem {chance} chances")
            print("*******************************")
            
        elif(menor):
            print("Você errou! O seu chute foi MENOR que o numero da CPU")
            chance = chance -1
            print(f"Voce tem {chance} chances")
            print("*******************************")
    if(chance==0):
            print("\nVocê Perdeu =/")
            print("\nFIM DO JOGO!!!")