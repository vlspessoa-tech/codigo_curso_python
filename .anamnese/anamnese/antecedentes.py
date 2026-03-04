habitos = []   # ou {} se você preferir dict
def hpp():
    return input('Digite a sua história da doença prévia: ').capitalize()

def obter_cirurgias(cirurgias):
    cirurgias = input('O paciente já foi submetido a alguma cirurgia? [S] para sim ou [N] para não: ')
    if cirurgias.lower() == 's':
        cirurgias = input('Digite as cirurgias que o paciente já foi submetido: ')  
    else:
        cirurgias = 'Nega cirurgias prévias'
    return cirurgias

def obter_alergias(alergias):
    alergias = input('Tem alergias: [S] para sim ou [N] para não): ')
    if alergias.lower() == 's':
        alergias = input('Digite as alergias do paciente: ')    
    else:    
        alergias = 'Desconhece alergias'
    return alergias

def obter_habitos(habitos):
    habitos_gerais = []

    while True:
        opcao = input(
            'Faz uso de drogas, álcool ou tabaco? '
            '[D] drogas, [A] álcool, [T] tabaco, [N] nenhum: '
            ).strip().lower()

        while opcao not in ('d', 'a', 't', 'n'):
            print('Opção inválida. Digite D, A, T ou N.')
            opcao = input(
                'Faz uso de drogas, álcool ou tabaco? '
                '[D] drogas, [A] álcool, [T] tabaco, [N] nenhum: '
                ).strip().lower()

            if opcao == 'n':
            # Se não usa nada, normalmente não faz sentido "adicionar outro"
                habitos_gerais = ['Nega uso de drogas, álcool ou tabaco']
                return habitos_gerais

            if opcao == 'd':
                sub = input(
                    'Canabis [M], Cocaína [C], Sintéticas [S], Anfetaminas [A], Outras [O]: '
                    ).strip().lower()

                while sub not in ('m', 'c', 's', 'a', 'o'):
                    print('Opção inválida. Digite M, C, S, A ou O.')
                    sub = input('Canabis [M], Cocaína [C], Sintéticas [S], Anfetaminas [A], Outras [O]: '
                    ).strip().lower()

                    if sub == 'm':
                        qtd = input('Quantas vezes por semana? ').strip()
                        habitos_gerais.append(f'Canabis, {qtd} vezes por semana')

                    elif sub == 'c':
                        qtd = input('Quantas vezes por semana? ').strip()
                        habitos_gerais.append(f'Cocaína, {qtd} vezes por semana')

                    elif sub == 's':
                        quais = input('Quais drogas sintéticas? ').strip()
                        qtd = input('Quantas vezes por semana? ').strip()
                        habitos_gerais.append(f'Drogas sintéticas ({quais}), {qtd} vezes por semana')

                    elif sub == 'a':
                        quais = input('Quais anfetaminas? ').strip()
                        qtd = input('Quantas vezes por semana? ').strip()
                        habitos_gerais.append(f'Anfetaminas ({quais}), {qtd} vezes por semana')

                    elif sub == 'o':
                        nome = input('Digite o nome da droga: ').strip()
                        qtd = input('Quantas vezes por semana? ').strip()
                        habitos_gerais.append(f'{nome}, {qtd} vezes por semana')

            elif opcao == 'a':
                qtd = input('Quantas doses por semana? ').strip()
                habitos_gerais.append(f'Álcool, {qtd} doses por semana')

            elif opcao == 't':
                while True:
                    qtde_cigarros = input('Quantos cigarros por dia? ').strip()
                    qto_anos = input('Há quantos anos? ').strip()
                    if qtde_cigarros.isdigit() and qto_anos.isdigit():
                        qtde_cigarros = int(qtde_cigarros)
                        qto_anos = int(qto_anos)
                        carga_tabagica = (qtde_cigarros / 20) * qto_anos
                        habitos_gerais.append(f'Tabaco, carga tabágica de {carga_tabagica:.1f} U.M.A.')
                        break
                print('Valores inválidos. Use apenas números inteiros.')

        # Pergunta se quer adicionar mais um hábito
        while True:
            acrescentar = input('Deseja adicionar outro hábito? [S] sim / [N] não: ').strip().lower()
            if acrescentar in ('s', 'n'):
                break
            print('Digite apenas S ou N.')

        if acrescentar == 'n':
            return habitos_gerais

        else:
            print('Nega uso de drogas, álcool ou tabaco')

def coletar(habitos):
    habitos = obter_habitos()
    return habitos

def obter_medicamentos(medicamentos):

    medicamentos = input('O paciente faz uso de medicamentos? [S] para sim ou [N] para não: ')
    if medicamentos.lower() == 's':
        medicamentos = input('Digite os medicamentos que o paciente faz uso: ')
    else:
        medicamentos = 'Nega uso de medicamentos'
    return medicamentos