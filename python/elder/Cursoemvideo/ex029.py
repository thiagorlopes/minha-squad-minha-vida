velo = float(input('Qual é a velocidade atual do carro? '))
if velo > 80:
    print(('VOCÊ FOI MULTADO! Voce excedeu o limite permitido que é de 80Km/h!'))
    print(f'Você deve pagar uma multa de R$ {(velo - 80) * 7:.2f}!')
print('Tenha um bom dia! Dirija com segurança!')
