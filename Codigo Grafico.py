'f(x) = |x²-3| [100 pontos, intervalo [-3 , 3]]'
import matplotlib.pyplot as plt
import math

Vi = -3
Vf = 3

np = 100

passo = (Vf-Vi)/np

x = []
y = []

for i in range(np+1):
    x.append(Vi)
    y.append(abs(Vi**2 - 3))
    Vi += passo
    
plt.figure(figsize=(8,6),dpi=100)
plt.plot(x,y)
plt.show()
