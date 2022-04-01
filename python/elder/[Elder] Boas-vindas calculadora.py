print('''Seja bem vindo à nossa calculadora!
Temos essas operações:
1. Soma
2. Subtração
3. Divisão
4. Multiplicação
5. Exponenciação''')
calculadora = int(input('Digite a operação desejada: '))
if calculadora == 1:
    n1 = float(input('Digite o primeiro número da soma: '))
    n2 = float(input('Digite o segundo número da soma: '))
    print(f'A soma dos números {n1} e {n2} é {n1 + n2}')
elif calculadora == 2:
    n1 = float(input('Digite o primeiro número da subtração: '))
    n2 = float(input('Digite o segundo número da subtração: '))
    print(f'A subtração dos números {n1} e {n2} é {n1 - n2}')
elif calculadora == 3:
    n1 = float(input('Digite o primeiro número da divisão: '))
    n2 = float(input('Digite o segundo número da divisão: '))
    print(f'A divisão do número {n1} por {n2} é {n1 / n2}')
elif calculadora == 4:
    n1 = float(input('Digite o primeiro número da multiplicação: '))
    n2 = float(input('Digite o segundo número da multiplicação: '))
    print(f'A multiplicação entre os números {n1} e {n2} é {n1 * n2}')
elif calculadora == 5:
    n1 = float(input('Digite o número a ser exponenciado: '))
    n2 = float(input('Digite a potência do número: '))
    print(f'A potenciação do número {n1} pelo número {n2} é {n1 ** n2}')
else:
    print('Você precisa escolher uma operação!')
print('Obrigado por escolher a nossa calculadora! Esperamos que tenha resolvido o seu problema matemático!')

