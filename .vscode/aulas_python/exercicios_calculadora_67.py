
'''
while True:
    try:
        numero_um = float(input('Digite um número:'))
        numero_dois = float(input('Digite outro número:'))
        
    except ValueError:
        print('Esse valor não é um número')
        continue
    operador = input('Digite um operador lógico: Ex: +, -, /, *: ')
    if operador == '+' or operador == '-' or operador == '/' or operador == '*':
            print (numero_um, operador, numero_dois)
    else:
            print('Esse operador não é o padrão.')
            continue
    if operador == '*':
        print(numero_um * numero_dois)
    elif operador == '-':
        print(numero_um - numero_dois)
    elif operador == '/':
         print(numero_um / numero_dois)
    else:
         print(numero_um + numero_dois)
       

    sair = input('Deseja sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break
    '''
while True:
    numero_1 = input('Digite um número:')
    numero_2 = input('Digite outro número:')
    operador = input('Digite um operador: *, -, / ou +:')

    numeros_validos = None
    
    try:
        numero_1 = float(numero_1)
        numero_2 = float(numero_2)
        operadores = '+' or '-' or '/' or '*'
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou mais parâmetros estão incorretos.')
        continue
    if operador == '+':
        print(numero_1 + numero_2)
    elif operador == '-':
        print(numero_1 - numero_2)
    elif operador == '/':
        print(numero_1 / numero_2)
    else:
        print(numero_1 * numero_2)

    sair = input('Deseja sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break