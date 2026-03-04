import os
palavra_secreta = 'perfume'
letras_acertadas = ''
tentativas = 0
while True:
        os.system('cls')
        letra_digitada = input('Digite uma letra:' )
        tentativas += 1

        if len(letra_digitada) > 1:
                print('Digite apenas uma letra.')
                continue

        if letra_digitada in palavra_secreta:
                letras_acertadas += letra_digitada

        palavra_formada = ''
        for letra_secreta in palavra_secreta:
                if letra_secreta in letras_acertadas:
                        palavra_formada += letra_secreta
                else: 
                        palavra_formada += '*'
        print(palavra_formada)
        if palavra_formada == palavra_secreta:
                print(f'Acertou! A palavra secreta é:',palavra_secreta)
                print('Com ',tentativas, 'tentativas')
                letras_acertadas = ''
                tentativas = 0



    
