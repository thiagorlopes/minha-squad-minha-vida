import random
a = str(input("Digite o nome do primeiro aluno: "))
b = str(input('Digite o nome do segundo aluno: '))
c = str(input('Digite o nome do terceiro aluno: '))
d = str(input('Digite o nome do quarto aluno: '))
list = [a, b, c, d]
print(f'O aluno sorteado foi {random.choice(list)}')
