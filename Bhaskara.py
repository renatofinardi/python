a = float(input())
b = float(input())
c = float(input())

delta =  b**2 - 4*a*c
print(f'Delta = {delta:.2f}')

if delta>0:
    raiz_delta = delta**0.5
    x1 = (-b + raiz_delta)/(2*a)
    x2 = (-b - raiz_delta)/(2*a)
    print(f'As raízes do polinômio são reais e distintas, sendo {x1:.2f} e {x2:.2f}')
elif delta == 0:
    x12 = -b/(2*a)
    print(f'As raízes do polinômio são reais e iguais, sendo {x12:.2f}')
else:
    Re = -b/(2*a)
    Im = ((-delta)**0.5/(2*a))
    print(f'O polinômio não possui raízes reais, sendo {Re:.2f}+{Im:.2f}i e {Re:.2f}-{Im:.2f}i')



    
