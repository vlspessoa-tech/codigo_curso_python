from . import ident, antecedentes, QPal, hda, exame_neurologico, exame_fisico

def escolher_local():
    while True:
        e = input('O paciente é de urgência ou ambulatorial? (U/A) ').strip().upper()
        if e in ('U', 'A'):
            return e
        print('Opção inválida. Digite U ou A.')

def executar():
    local = escolher_local()

    # ident.definir_nome()              # você precisa ter isso no ident.py
    # ident.definir_idade()
    # ident.definir_sexo()
    # ident.autonomia()
    # ident.profissao()
    antecedentes.hpp()
    antecedentes.obter_cirurgias(cirurgias=True)
    antecedentes.obter_alergias(alergias=True) 
    antecedentes.obter_habitos(habitos=True)
    antecedentes.obter_medicamentos(medicamentos=True)
    # QPal.coletar(local)
    # hda.hda()   
    # hda.nega_sintomas()
    # exame_fisico.estado_geral()
    # exame_fisico.estado_atual()
    # exame_fisico.sinais_vitais()
    # exame_neurologico.coleta_lucidez(lucidez={})  
    # exame_neurologico.coleta_orientacao(orientacao={})
    # exame_neurologico.coleta_linguagem(linguagem={})
    # exame_neurologico.coleta_memoria(memoria={})
    # exame_neurologico.coleta_comportamento(comportamento={})
    # exame_neurologico.estado_mental(dict={})
    # antecedentes.coletar()
    
    if local == 'U':
        print(montar_impressoes_urgencia())
    else:
        print(montar_impressoes_ambulatorio())

def montar_impressoes_urgencia():
    #sv = exame_fisico.sinais_vitais()
    bold = "\033[1m"
    reset = "\033[0m"
    return (
        #f'\n{bold}Identificação:{reset}\n{"\n".join([f"{chave}: {valor}" for chave, valor in ident.dados_paciente.items()])}\n'
        # f'Queixa principal: {QPal.queixa_principal_urgencia}\n'
        # f'História de doença prévia: {antecedentes.hpp()}\n'
        # f'História de doença atual: {hda.hda()}\n'
        f'\n{bold}História de doença prévia:{reset} {antecedentes.hpp()}\n'
        f'\n{bold}Cirurgias prévias:{reset} {antecedentes.obter_cirurgias()}\n'
        f'\n{bold}Alergias:{reset} {antecedentes.obter_alergias()}\n'
        f'\n{bold}Hábitos:{reset} {", ".join([f"- {item}" for item in antecedentes.habitos]) if antecedentes.habitos else "Não informado"}\n'
        f'\n{bold}Medicamentos:{reset} {antecedentes.obter_medicamentos()}\n'
        # f'Nega sintomas: {hda.nega_sintomas()}\n'
        # f'Estado geral do paciente: {exame_fisico.estado_geral()}\n'
        # f'Estado atual do paciente: {exame_fisico.estado_atual()}\n'
        # f'Sinais vitais:\n'
        # f'- Temperatura: {sv["temperatura"]}°C\n'
        # f'- Pressão arterial: {sv["pressao_arterial"]} mmHg\n'
        # f'- Frequência cardíaca: {sv["frequencia_cardiaca"]} bpm\n'
        # f'- Frequência respiratória: {sv["frequencia_respiratoria"]} rpm\n'
        # f'- Saturação de oxigênio: {sv["saturacao_oxigenio"]} %\n'
        # f'- Score de Glasgow: {sv["glasgow"]}\n'
        # f'Exame neurológico: \n'
        # f'- Lucidez: {exame_neurologico.coleta_lucidez(lucidez={})}\n'
        # f'- Orientação: {exame_neurologico.coleta_orientacao(orientacao={})}\n'
        # f'- Linguagem: {exame_neurologico.coleta_linguagem(linguagem={})}\n'
        # f'- Memória: {exame_neurologico.coleta_memoria(memoria={})}\n'
        # f'- Comportamento: {exame_neurologico.coleta_comportamento(comportamento={})}\n'
        # f'- Estado mental: {exame_neurologico.estado_mental(dict={})}\n'
    )

def montar_impressoes_ambulatorio():
    return (
        f'Identificação: {", ".join([f"{chave}: {valor}" for chave, valor in ident.dados_paciente.items()])}\n'
        f'Queixa principal: {QPal.queixa_principal_ambulatorio}\n'
        f'História de doença prévia: {antecedentes.hpp}\n'
        f'Cirurgias prévias: {antecedentes.cirurgias}\n'
        f'Alergias: {antecedentes.alergias}\n'
        f'Hábitos: {", ".join([f"- {chave}: {valor}" for chave, valor in antecedentes.habitos.items()])}\n'
        f'Medicamentos: {antecedentes.medicamentos}\n'
        f'História de doença atual: {antecedentes.hda}\n'
        f'Nega sintomas: {hda.nega_sintomas}\n'
        f'Estado geral do paciente: {exame_fisico.estado_geral()}\n'
        f'Estado atual do paciente: {exame_fisico.estado_atual()}\n'
        f'Temperatura: {exame_fisico.sinais_vitais["temperatura"]}°C\n'
        f'Pressão arterial: {exame_fisico.sinais_vitais["pressao_arterial"]} mmHg\n'
        f'Frequência cardíaca: {exame_fisico.sinais_vitais["frequencia_cardiaca"]} bpm\n'
        f'Frequência respiratória: {exame_fisico.sinais_vitais["frequencia_respiratoria"]} irpm\n'
        f'Saturação de oxigênio: {exame_fisico.sinais_vitais["saturacao_oxigenio"]} %\n'
        f'Score de Glasgow: {exame_fisico.sinais_vitais["glasgow"]}\n'
        f'Exame neurológico: {exame_neurologico.resultado}'
    )

    
    