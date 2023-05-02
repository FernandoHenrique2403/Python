import random 
def jogar_adivinha():
        
    print("*******************************")
    print("**--** Bem Vindo ao Jogo **--**")
    print("*******************************")
    print("\n")

    numero_CPU = round(random.randrange(1,101))
    pontos = 1000
    print(numero_CPU)
    chance = 0
    nivel = int(input("Qual dificuldade quer jogar? \n1 - Fácil \n2 - Médio \n3 - Difícil "))

    if(nivel == 1):
        chance = 20
    elif(nivel ==2):
        chance = 10
    elif(nivel == 3):
        chance =3


    while(chance>0):
        chute = int(input("Digite o Numero do seu Chute : "))
        print("Você digitou : ",chute)

        acertou = numero_CPU == chute
        maior = chute > numero_CPU
        menor = chute < numero_CPU
        if(acertou):
            print("Você Acertou !!")
            print("\nFIM DO JOGO!!!")
            print("Pontuação : {}".format(pontos))
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
            calcula_pontos =  abs(chute-numero_CPU)
            pontos = pontos - calcula_pontos    
        if(chance==0):
                print(numero_CPU)
                print("\nVocê Perdeu =/")
                print("Pontuação : {}".format(pontos))
                print("\nFIM DO JOGO!!!")
                
if(__name__=="__main__"):
    jogar_adivinha()