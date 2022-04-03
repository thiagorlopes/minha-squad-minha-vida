dias = int(input('Quantos dias alugados? '))
kmr = float(input('Quantos km rodados? '))
print(f'O total a pagar é de R${dias * 60 + kmr * 0.15:.2f}')
