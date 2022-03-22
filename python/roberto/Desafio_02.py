# 1.	Crie um script que conte o número de vogais em uma string inserida pelo usuário
texto=str(input('entre com uma frase: ')).strip().upper()
vogais=['A','E','I','O','U']
char=list(texto)
i=0
for j in range(len(char)):
    if char[j] in vogais:
        i+=1
if i>0:
    print(f'{i} vogais encontradas')
else:
    print('Nehuma vogal encontrada')
    
#2.	Crie um script que inverte uma palavra se ela tiver um número par de caracteres ou que a imprima normalmente se ímpar 
texto=str(input('entre com uma frase: ')).strip().upper()
char=list(texto)
if len(char)%2 == 0:
    texto=texto[::-1]
print(texto.lower())

       
