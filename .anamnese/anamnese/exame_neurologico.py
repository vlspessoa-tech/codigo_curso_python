def pergunta_sn(texto: str) -> bool:
    """Pergunta (s/n) e valida entrada."""
    while True:
        resp = input(texto).strip().lower()
        if resp.startswith('s'):
            return True
        if resp.startswith('n'):
            return False
        print("Entrada inválida. Responda com 's' ou 'n'")

def multi_escolha(titulo: str, opcoes: list[str]) -> list[str]:
    """Permite selecionar múltiplas opções pelo número, sem duplicar."""
    escolhas = []  # Valor padrão

    while True:
        print(f"\n{titulo}")
        for i, opcao in enumerate(opcoes, 1):
            print(f"{i}. {opcao}")

        entrada = input("Digite o número da opção: ").strip()
        if not entrada.isdigit():
            print("Digite um número válido.")
            continue

        indice = int(entrada) - 1
        if not (0 <= indice < len(opcoes)):
            print("Opção inválida.")
            continue

        opcao_escolhida = opcoes[indice]
        if opcao_escolhida not in escolhas:
            escolhas.append(opcao_escolhida)
            
        else:
            print("Essa opção já foi adicionada.")

        if not pergunta_sn("Deseja adicionar outra opção? (s/n) "):
            break

    return escolhas

def coleta_lucidez(lucidez) -> str:
    while True:
        resp = input("Estado mental do paciente? "
        "[L] Lúcido, [C] Confuso, [S] Sonolento, [I] Irritável, [O] Outros: ").strip().upper()

        mapa = { "L": "- Lúcido", "C": "- Confuso", "S": "- Sonolento", "I": "- Irritável",}

        if resp in mapa:
            return mapa[resp]

        if resp == "O":
            outro = input("Descreva o estado mental do paciente: ").strip().capitalize()
            return outro if outro else "Outros"

        print("Opção inválida. Use L, C, S, I ou O.")

def coleta_orientacao(orientacao) -> list[str]:
    tempo = pergunta_sn("O paciente está orientado no tempo? (s/n) ")
    espaco = pergunta_sn("O paciente está orientado no espaço? (s/n) ")
    pessoa = pergunta_sn("O paciente está orientado em relação à pessoa? (s/n) ")

    resultado = []

    if tempo:
        resultado.append("Orientado no tempo")
    else:
        resultado.append("Desorientado no tempo")

    if espaco:
        resultado.append("Orientado no espaço")
    else:
        resultado.append("Desorientado no espaço")

    if pessoa:
        resultado.append("Orientado em pessoa")
    else:
        resultado.append("Desorientado em pessoa")

    return resultado

def coleta_linguagem(linguagem):
    if not pergunta_sn("O paciente apresenta alterações na linguagem? (s/n) "):
        return '- Sem alterações'

    opcoes = ["Dislalia", "Disartria", "Afasia motora (Broca)", "Afasia sensitiva (Wernicke)",
        "Afasia de condução", "Afasia anômica", "Afasia global",]
    return multi_escolha("Alterações de linguagem:", opcoes)

def coleta_memoria(memoria):
    if not pergunta_sn("O paciente apresenta alterações na memória? (s/n) "):
        return '- Sem alterações'

    opcoes = [
        "Amnésia anterógrada", "Amnésia retrógrada", "Amnésia global", "Amnésia lacunar", "Alteração de memória recente", 
        "Alteração de memória remota", "Delírium", "Estado pós-ictal", "Outros",]
    escolhas = multi_escolha("Alterações de memória:", opcoes)

    if "Outros" in escolhas:
        outro = input("Descreva 'Outros' (memória): ").strip()
        if outro:
            escolhas[escolhas.index("Outros")] = f"Outros: {outro}"

    return escolhas

def coleta_comportamento(comportamento):
    if not pergunta_sn("O paciente apresenta alterações no comportamento? (s/n) "):
        return '- Sem alterações'

    opcoes = [
        "Agitação psicomotora", "Apatia", "Depressão", "Euforia", "Ansiedade", "Pânico",
        "Fobia", "Compulsão", "Delírio", "Alucinação", "Ilusão", "Paranóia", "Irritabilidade",
        "Hostilidade", "Agressividade", "Outros", ]

    escolhas = multi_escolha("Alterações de comportamento:", opcoes)

    if "Outros" in escolhas:
        outro = input("Descreva 'Outros' (comportamento): ").strip()
        if outro:
            escolhas[escolhas.index("Outros")] = f"Outros: {outro}"

    return escolhas

def estado_mental(dict):
    lucidez = coleta_lucidez(None)
    orientacao = coleta_orientacao([])
    linguagem = coleta_linguagem([])
    memoria = coleta_memoria([])
    comportamento = coleta_comportamento([])

    return {"Paciente": lucidez,
        "Orientação": orientacao,
        "Linguagem": linguagem,
        "Memória": memoria,
        "Comportamento": comportamento
    }


    print(f"{chave}:")
    
    if isinstance(valor, list):
        if not valor:
            print("  Sem alterações")
        else:
            for item in valor:
                print(f"  - {item}")
    
    elif isinstance(valor, dict):
        for sub_chave, sub_valor in valor.items():
            status = "Orientado" if sub_valor else "Desorientado"
            print(f"  - {status} no {sub_chave}")
    
    else:
        print(f"  {valor}")

    print()  # linha em branco entre blocos

#Acabou esse. Tá lindo! Agora é só integrar com o restante do sistema.