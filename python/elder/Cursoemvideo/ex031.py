dist = float(input('Qual é a distância da sua viagem? '))
print (f'Você está prestes a fazer uma viagen de {dist:.2f} Km. ')
if dist < 200:
    p = dist * 0.50
else:
    p = dist * 0.45
print(f'O preço da sua passagem será de \033[32mR$ {p:.2f}\033[m')
