import random
import os

while not False:
    os.system("cls")
    print("Vamos começar o jogo.")
    print("\nPrimeiro: escolha uma das opcões sendo elas: PEDRA, PAPEL ou TESOURA.")
    
    #jogador 1
    jogador_1 = str(input("Qual sua opção: ")).lower()

    #jogador 2 
    opcoes = ["pedra","papel","tesoura"]
    jogador_2 = random.choice(opcoes)

    os.system("cls")

    if jogador_1 not in opcoes:
        print("Não temos essa opção. Tente novamente.")

    elif jogador_1 == jogador_2:
        print("Empate!")

    elif jogador_1 == "pedra" and jogador_2 == "tesoura" or jogador_1 == "papel" and jogador_2 == "pedra" or jogador_1 == "tesoura" and jogador_2 == "papel":
        print("Voce ganhou!")

    else:
        print("Você Perdeu!")

    
    print("\njogador 1:",jogador_1 )
    print("jogador 2:",jogador_2)

    novamente = input("\nDeseja jogar novamente: \"S\" pra \"SIM\" ou \"N\" pra \"NÃO\": ").lower()
    if novamente == "n":
        print("Obrigado por jogar <3")
        break
