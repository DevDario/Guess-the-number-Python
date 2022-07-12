import random

def header():
    print('***********************')
    print('**GUESS THE NUMBER**')
    print('***********************\n')

tentativas_nivel1=20
tentativas_nivel2=10
tentativas_nivel3=5
secret_number= random.randrange(0,100)

print('***********************')
print('**GUESS THE NUMBER**\n')
print('**      MAIN MENU    **')
print('***********************\n')
print('1- Level 1(20 tentativas)\n')
print('2- Level 2(10 tentativas)\n')
print('3- Level 3(5 tentativas)\n')
escolha=int(input(':'))

while(escolha!=0):
    level1=escolha==1
    level2=escolha==2
    level3=escolha==3


    if (level1):
        rodada=1
        while(rodada <= tentativas_nivel1):
            header()
            print('Rodada {} de {}'.format(rodada,tentativas_nivel1))
            user_number=int(input('Digite um número:'))
            if (user_number==secret_number):
                print('Acertou !, o número secreto é {}'.format(secret_number))
                escolha=0
                break
            elif(user_number>secret_number):
                print('Quase ! você digitou um número maior maior que o número secreto.')
            elif(user_number<secret_number):
                print('Quase ! você digitou um número menor que o número secreto.')

                
                rodada = rodada +1
                if(rodada>=tentativas_nivel1):
                    print('Fim do jogo')
                    escolha=0

    elif(level2):
        rodada=1
        while(rodada <= tentativas_nivel2):
            header()
            print('Rodada {} de {}'.format(rodada,tentativas_nivel2))
            user_number=int(input('Digite um número:'))
            if (user_number==secret_number):
                print('Acertou !, o número secreto é {}'.format(secret_number))
                escolha=0
                break
            elif(user_number>secret_number):
                print('Quase ! você digitou um número maior maior que o número secreto.')
            elif(user_number<secret_number):
                print('Quase ! você digitou um número menor que o número secreto.')

                rodada = rodada +1
                if(rodada>=tentativas_nivel2):
                    print('Fim do jogo')
                escolha=0
                 
    elif(level3):
        rodada=1
        while(rodada <= tentativas_nivel3):
            print('***********************')
            print('**GUESS THE NUMBER**')
            print('***********************\n')

            print('Rodada {} de {}'.format(rodada,tentativas_nivel3))
            user_number=int(input('Digite um número:'))
            if (user_number==secret_number):
                print('Acertou !, o número secreto é {}'.format(secret_number))
                escolha=0
                break
            elif(user_number>secret_number):
                print('Quase ! você digitou um número maior maior que o número secreto.')
            elif(user_number<secret_number):
                print('Quase ! você digitou um número menor que o número secreto.')

                rodada = rodada +1
                if(rodada>=tentativas_nivel3):
                    print('Fim do jogo')
                escolha=0