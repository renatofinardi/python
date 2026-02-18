def desconto(idade, carteira_estudante):
    if idade<5:
        print(f'Entrada gratuita')
    else:
        if carteira_estudante == "S" or carteira_estudante == "s" or idade>60:
            print(f'Meia-entrada')
        elif carteira_estudante == "N" or carteira_estudante == "n":
            print(f'Inteira')
        else:
            print(f'Erro: Entrada "{carteira_estudante}" inválida. Use apenas S ou N.')

def main():
    idade = int(input())
    carteira_estudante = input()
    desconto(idade, carteira_estudante)
main()