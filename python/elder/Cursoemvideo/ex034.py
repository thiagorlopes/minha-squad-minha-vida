soldo = float(input('Qual é o salário do funcionácio? R$ '))
if soldo <= 1250:
    novo = soldo * 1.15
else:
    novo = soldo * 1.10
print(f'Quem ganhava R$ {soldo:.2f} passa a ganhar R$ {novo:.2f} agora.')
