"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

while True:
    cpf = input('Digite o número do seu CPF: (somente números)')
    if cpf.isdigit() and len(cpf) == 11:
        break
    else:
        print('CPF inválido. Digite exatamente 11 números.')
cpf_bruto = [int(d) for d in cpf]
print ('O CPF é: ', cpf_bruto)
    
cpf_nove_digitos = cpf_bruto[:9]
print('Os 9 primeiros números do seu CPF é: ',*cpf_nove_digitos)

soma_nove_digitos = 0
contagem_regerssiva = 10

for digito in cpf_nove_digitos:
    soma_nove_digitos += digito * contagem_regerssiva
    contagem_regerssiva -= 1
   # print(soma_nove_digitos, contagem_regerssiva)

multiplicado_dez = soma_nove_digitos * 10
print(f'A soma dos nove dígitos é: {soma_nove_digitos}')
print(f'O número anterior multiplicado por 10 é: {multiplicado_dez}')
resto_divisao = multiplicado_dez % 11
if resto_divisao > 9:
    print('O resultado é zero.')
else:
    print('O primeiro dígito do seu CPF é: ',resto_divisao)

cpf_dez_digitos = cpf_bruto[:10]
print('Os 10 primeiros números do seu CPF é: ',*cpf_dez_digitos)
soma_dez_digitos = 0
contagem_regerssiva = 11

for digito in cpf_dez_digitos:
    soma_dez_digitos += digito * contagem_regerssiva 
    contagem_regerssiva -= 1
multiplicado_dez = soma_dez_digitos * 10
print(f'A soma dos dez dígitos é: {soma_dez_digitos}')
print(f'O número anterior multiplicado por 10 é: {multiplicado_dez}')
resto_divisao2 = multiplicado_dez % 11
if resto_divisao2 > 9:
    print('O resultado é zero.')
else:
    print('O segundo dígito do seu CPF é: ',resto_divisao2)


if resto_divisao == cpf_bruto[9] and resto_divisao2 == cpf_bruto[10]:
    print('CPF válido!')
else:
    print('CPF inválido!')

print(cpf_nove_digitos, resto_divisao, resto_divisao2)