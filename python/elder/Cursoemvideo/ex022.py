nome = str(input('Qual seu nome completo: ')).strip()
primeiro = nome.split()
print(f'''Seu nome com todas as letras maíusculas: {nome.upper()}
Seu nome com todas as letras minúsculas: {nome.lower()}
Seu nome possui {len(nome) - nome.count(' ')} letras ao todo (sem considerar espaços)
Seu primeiro nome é {primeiro[0]} e ele possui {len(primeiro[0])} letras''')
