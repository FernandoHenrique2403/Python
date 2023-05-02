def jogar_forca():
    print("*******************************")
    print("**--** Bem Vindo ao Jogo **--**")
    print("*******************************")
    print("\n")

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]
    enforcou = False
    acertou = False
    print(letras_acertadas)
    
    while(not enforcou and not acertou):
        
        chute = input("Qual letra? ")
        chute = chute.strip()
        
        
        index =0

        for letra in palavra_secreta:
            if(letra.upper() == chute.upper()):
                letras_acertadas[index] = letra
                print(letras_acertadas)
                letras_faltando = str(letras_acertadas.count('_'))
                print( 'Ainda faltam acertar {} letras'.format(letras_faltando))         
            index = index+1
            
if(__name__=="__main__"):
    jogar_forca()