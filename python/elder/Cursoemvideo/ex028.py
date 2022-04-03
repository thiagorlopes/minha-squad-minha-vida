import random
import time
pc = random.randint(0, 5)
print('-.-' * 30)
print('Vou pensar em um número entre 0 e 5, tente adivinha-lo!')
print('-.-' * 30)
gamer = int(input('Em que número pensei? '))
print('PROCESSANDO.')
time.sleep(1)
print('PROCESSANDO..')
time.sleep(1)
print('PROCESSANDO...')
time.sleep(1)
if gamer == pc:
    print(f'Parabéns! Você ganhou, eu também pensei no número {pc}')
else:
    print(f'Que triste, eu pensei no número {pc} e não no número {gamer}')
