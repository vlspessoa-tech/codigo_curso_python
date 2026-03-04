def estado_geral():
    estado_geral = input('Estado geral no momento? [B] Bom, [R] Regular, [M] Mau] ')
    if estado_geral.upper() == 'B':
        estado_geral = 'Bom'
    elif estado_geral.upper() == 'R':
        estado_geral = 'Regular'
    elif estado_geral.upper() == 'M':
        estado_geral = 'Mau'
    return estado_geral

def estado_atual():
    estado_atual = ['Tóxico', 'Sudado', 'Prostrado', 'Confuso', 'Dor evidente', 'Dispneico', 'Outros' ]
  
    print('Selecione o estado atual do paciente:')
    for i, opcao in enumerate(estado_atual, 1):
        print(f'{i}. {opcao}')
    escolha = int(input('Digite o número da opção desejada: ')) - 1
    if 0 <= escolha < len(estado_atual):
        return escolha
    else:
        return 'Opção inválida'
    
def glasgow():
    glasgow = ['Olhos: 1- Não abre, 2- Abre ao estímulo doloroso, 3- Abre ao comando verbal, 4- Abre espontaneamente',
              'Verbal: 1- Não emite som, 2- Emite sons incompreensíveis, 3- Emite palavras inapropriadas, 4- Emite palavras confusas, 5- Orientado',
              'Motora: 1- Não obedece, 2- Extensão anormal, 3- Flexão anormal, 4- Retirada ao estímulo doloroso, 5- Localiza a dor, 6- Obedece comandos'
              ]
    while True:
        try:
            resposta_olhos = int(input('Digite a resposta dos olhos (1-4): '))
            resposta_verbal = int(input('Digite a resposta verbal (1-5): '))
            resposta_motora = int(input('Digite a resposta motora (1-6): '))
            if 1 <= resposta_olhos <= 4 and 1 <= resposta_verbal <= 5 and 1 <= resposta_motora <= 6:
                glasgow_total = resposta_olhos + resposta_verbal + resposta_motora
                return f'{resposta_olhos} + {resposta_verbal} + {resposta_motora} = {glasgow_total}'
            else:
                print('Respostas devem estar dentro dos intervalos especificados. Tente novamente.')
        except ValueError:
            print('Entrada inválida. Por favor, digite um número inteiro.')
        return glasgow
    
def sinais_vitais():
    return {
        'temperatura': input('Digite a temperatura do paciente: '),
        'pressao_arterial': input('Digite a pressão arterial do paciente: '),
        'frequencia_cardiaca': input('Digite a frequência cardíaca do paciente: '),
        'frequencia_respiratoria': input('Digite a frequência respiratória do paciente: '),
        'saturacao_oxigenio': input('Digite a saturação de oxigênio do paciente: '),
        'glasgow': glasgow()
    }

