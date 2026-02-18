def emprestimo(idade, renda, situacao):
    if not(18<=idade<=65):
        print(f'Idade não permitida para empréstimo')
    else:
        if situacao == "N" or situacao == "n":
            print(f'Empréstimo: Negado')
        elif situacao == "S" or situacao == "s":
            if renda<2000:
                print(f'Empréstimo: Negado')
            elif 2000<=renda<=5000:
                print(f'Empréstimo: Aprovado Bronze')
            else:
                print(f'Empréstimo: Aprovado Gold')
        else:
            print(f'Erro: Entrada {situacao} inválida. Use apenas S(s) ou N(n)')
    
def main():
    idade = int(input())
    renda = float(input())
    situacao = input()
    emprestimo(idade, renda, situacao)
main()