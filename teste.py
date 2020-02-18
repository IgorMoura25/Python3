def jogar():

    print("********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("********************************")

    palavra_secreta = "banana"

    letras_acertadas = ["_","_","_","_","_","_"]

    enforcou = False
    acertou = False

    #Enquanto não enforcou e não acertou
    while(not enforcou and not acertou):
        
        chute = input("Qual letra?")
        chute = chute.strip().lower()



        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                letras_acertadas[index] = letra

            index = index + 1
        
        print(letras_acertadas)

    print("Fim de jogo")
    
if(__name__ == "__main__"):
    jogar()
