print('Verificador de Triângulos')
reta1 = float(input('Tamanho da primeira reta: '))
reta2 = float(input('Tamanho da segunda reta: '))
reta3 = float(input('Tamanho da terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Com os valores informados acima, existe um triângulo!')
else:
    print('Com os valores informados acima, NÂO existe um triângulo')
