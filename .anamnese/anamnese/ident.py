dados_paciente = {}

def definir_nome():
    global dados_paciente
    resp = input("Deseja definir o nome do utente? (s/n) ").strip().lower()
    if resp == "s":
        nome = input("Nome: ").strip()
        dados_paciente["Nome"] = nome
        return dados_paciente
    else:
        nome = "Não informado"
        dados_paciente["Nome"] = nome
    return dados_paciente

def definir_idade():
    idade_paciente = input('Digite a idade do paciente: ')
    try:
        idade = int(idade_paciente) 
        dados_paciente["Idade"] = idade
    except ValueError:
        print('Idade inválida. Digite novamente.')
        return definir_idade()
    return dados_paciente

def definir_sexo():
    sexo_paciente = input('Digite o sexo do paciente (M/F): ')
    if sexo_paciente.upper() == 'M':
        sexo = 'Masculino'
        dados_paciente["Sexo"] = sexo
        return dados_paciente
    elif sexo_paciente.upper() == 'F':
        sexo = 'Feminino'
        dados_paciente["Sexo"] = sexo
        return dados_paciente
    else:
        print('Opção inválida. Digite novamente.')
        return definir_sexo()
    
def autonomia():
    print('O paciente é autônomo? (s/n)')
    autonomia_paciente = input('Digite [S] para sim ou [N] para não: ')
    
    if autonomia_paciente.lower() == 's':
        autonomia = 'Paciente é autônomo'
        dados_paciente["Autonomia"] = autonomia
        return dados_paciente
    elif autonomia_paciente.lower() == 'n':
        totalmente_dependente = input('O utente é totalmente dependente? (s/n)')
        if totalmente_dependente.lower() == 's':
            dados_paciente["Autonomia"] = "Utente é totalmente dependente"
            return dados_paciente
        else:
            dados_paciente["Autonomia"] = "Utente é parcialmente dependente"
            return dados_paciente
    else:
        print('Opção inválida. Digite novamente.')
        return autonomia()

def profissao():
    profissao_paciente = input('Digite a profissão do utente: ')
    if profissao_paciente.strip() == '':
        profissao = 'Não informado'
        dados_paciente["Profissão"] = profissao
        return dados_paciente
    else:
        profissao = profissao_paciente
    dados_paciente["Profissão"] = profissao
    return dados_paciente

#CONCLUIDO
