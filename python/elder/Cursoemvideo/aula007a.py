#operadores aritméticos
# + = adição
# - = subtração
# * = multiplicação
# / = divisão
# ** = potência
# // = Divisão inteira
# % = resto da divisão
#raiz quadrada elevar a 1/2, raiz cúbica elevar a 1/3 ...
#alinhar a esquerda <, direita>, centralizado ^
#para quebrar a linha \n, para não quebrar a linha ,end=''

#ordem = precedência
# 1 = ()
# 2 = **
# 3 = *, /, //, %
# 4 = +, -

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
dr = n1 % n2
e = n1 ** n2
print(f'A soma é {s}, o produto é {m}, a divisão é {d}, a divisão inteira é {di}, o resto da divisão é {dr},  o número {n1} elevado a {n2}, resulta em {e}')