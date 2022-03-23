import math

an = float(input('Digite o ângulo a ser analisado: '))
a = math.radians(an)
print(f'Para o ângulo {a:.2f}° temos o SENO {math.sin(a):.2f}, o COSSENO {math.cos(a):.2f} e a TANGENTE {math.tan(a):.2f}')