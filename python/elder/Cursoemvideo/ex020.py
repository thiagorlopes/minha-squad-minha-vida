import random
a = str(input("Digite o nome do primeiro aluno: "))
b = str(input('Digite o nome do segundo aluno: '))
c = str(input('Digite o nome do terceiro aluno: '))
d = str(input('Digite o nome do quarto aluno: '))
list = [a, b, c, d]
random.shuffle(list)
print(f'A ordem de apresentação dos trabalhos é {list}')
