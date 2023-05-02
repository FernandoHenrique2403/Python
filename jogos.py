import forca
import Dificuldade

def escolhe_jogo():
    print("*******************************")
    print("**--** Escolha seu jogo! **--**")
    print("*******************************")
    print("\n")
    print("1 - Forca \n2 - Adivinhação")
    jogo = int(input("Qual Jogo?  "))

    if(jogo != 1 and jogo !=2):
        print("Código Errado")
    elif(jogo == 1):
        print("Jogando Forca")
        forca.jogar_forca()
    elif(jogo == 2):
        print("Jogando Adivinhação")
        Dificuldade.jogar_adivinha()
if(__name__=="__main__"):
    escolhe_jogo()