import math
# from math import hypot
co = float(input('Digite o comprimento do cateto oposto em cm: '))
ca = float(input('DIgite o comprimento do cateto adjacente em cm: '))
print(f'Com os valores informados do cateto oposto de {co}cm e cateto adjacente de {ca}cm, a hipotenusa desse triângulo retângulo é de {math.hypot(ca, co):.2f}cm')