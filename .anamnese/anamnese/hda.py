def hda():
    return input('Digite a sua história da doença atual: ')

def nega_sintomas():
    nega = ['Cefaléia', 'Tontura', 'Náusea', 'Vômito', 'Dor torácica', 'Dispneia', 'Palpitação', 
        'Edema', 'Síncope', 'Convulsão', 'Ortopneia', 'Dificuldade para urinar', 'Dificuldade para evacuar', 
        'Dor abdominal', 'Diarreia', 'Obstipação', 'Febre', 'Calafrios', 'Sudorese noturna', 
        'Perda de peso', 'Ganho de peso', 'DPN', 'Disúria', 'Polaquiúria', 'Hematúria', 'Exantema',
        'Prurido', 'Estrangúria', 'Polidipsia', 'Polifagia', 'Fadiga', 'Fraqueza', 'Anorexia', 'Astenia',
        'Parestesia', 'Hiperestesia', 'Paresia', 'Traumas', 'Quedas', 'Tosse', 'Expectoração', 'Hemoptise',
        'Disfagia', 'Rouquidão', 'Melena', 'Hematoquezia', 'Hematemese', 'Outros sintomas'
    ]
    for i, sintoma in enumerate(nega, 1):
        print(f"{i}. {sintoma}")
        nega_sintomas = []
    while True:
        entrada = input("Digite o número do sintoma que o paciente apresenta (ou '0' para finalizar): ").strip()
        if entrada == '0':
            break
        if not entrada.isdigit():
            print("Digite um número válido.")
            continue

        indice = int(entrada) - 1
        if not (0 <= indice < len(nega)):
            print("Número fora do intervalo. Tente novamente.")
            continue

        sintoma_escolhido = nega[indice]
        if sintoma_escolhido not in nega_sintomas:
            nega_sintomas.append(sintoma_escolhido)
        else:
            print("Esse sintoma já foi adicionado.")


#nesssa sessao a opcao nega sintomas apresenta duas soluções, 
# fica pendente a escolha da melhor forma de apresentar os sintomas negados, 
# se a partir da escolha do numero ou a partir da resposta sim ou nao para cada sintoma