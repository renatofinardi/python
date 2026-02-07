x = float(input())

resultado = 0
n = 20
fat = 1

for i in range(n):
    if i>0:
        fat *= i
    resultado += (x**i)/fat

print(f'e elevado a {x:.2f} vale {resultado:.5f}')