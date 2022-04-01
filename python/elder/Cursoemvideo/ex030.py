n = int(input('Me diga um número qualquer avulso: '))
res = n % 2
if res == 0:
    print(f'0 número {res} é \033[34mPAR\033[m')
else:
    print(f'0 número {res} é \033[3;31mÍMPAR\033[m')
