import hashlib
import string

def criar():
    while True:
        senha = input('Crie sua senha de 8 digitos ou mais: contendo leras maiusculas, minúsculas, letras, numeros, cararteres!\n  ').strip()
        tamanho = len(senha) >= 8 
        numeros = any(char.isdigit() for char in senha) 
        maiusculas = any(char.isupper() for char in senha) 
        minusculas = any(char.islower() for char in senha) 
        caracteres = any(char in string.punctuation for char in senha)

        if tamanho and numeros and maiusculas and minusculas and caracteres:
            print('Senha válida!')
            return senha
        else:
            print('Senha inválida! ')

def gerar_hash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def compara_senha(hash):
    login = input('Digite sua senha!')
    if gerar_hash(login) == hash:
        print("Login correto")
    else:
        print("Senha incorreta")
    

senha = criar()
compara = compara_senha(hash)

print(senha, compara)

