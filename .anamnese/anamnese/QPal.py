# anamnese/QPal.py

queixa_principal_urgencia = ""
queixa_principal_ambulatorio = ""

def QP_urgencia():
    return input("Queixa principal (urgência): ").strip()

def QP_ambulatorio():
    return input("Queixa principal (ambulatorial): ").strip()

def coletar(local):  # local = "U" ou "A"
    global queixa_principal_urgencia, queixa_principal_ambulatorio
    if local == "U":
        queixa_principal_urgencia = QP_urgencia()
    else:
        queixa_principal_ambulatorio = QP_ambulatorio()