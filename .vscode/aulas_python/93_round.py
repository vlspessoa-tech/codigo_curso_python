'''numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)
0.7999999999999999

print(f'{numero_3:.2f}')
0.80

#ou

print(round(numero_3, 2))
0.8'''

import decimal
numero_1 = decimal.Decimal(0.1)
numero_2 = decimal.Decimal(0.7)
numero_3 = numero_1 + numero_2
print(numero_3)
#0.7999999999999999611421941381
