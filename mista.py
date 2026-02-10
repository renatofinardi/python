def mista(numerador: int, denominador: int):
    n = numerador//denominador
    frac = numerador%denominador
    print(f"{n}({frac}/{denominador})")

def main():
    numerador = int(input())
    denominador = int(input())
    if denominador == 0:
        print("ERRO")
    else:
        mista(numerador, denominador)

main()

