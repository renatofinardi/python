def salary(salario_atual, tempo_servico):
    if salario_atual < 1500:
        reajuste = salario_atual * 0.20
    elif salario_atual < 2000:
        reajuste = salario_atual * 0.15
    elif salario_atual < 6000:
        reajuste = salario_atual * 0.10
    else:
        reajuste = 0

    if tempo_servico < 1:
        bonus = 0
    elif 1<= tempo_servico <=3:
        bonus = 100
    elif 4<= tempo_servico <=6:
        bonus = 200
    elif 7<= tempo_servico <=10:
        bonus = 300
    else:
        bonus = 500

    novo = salario_atual + reajuste + bonus
    if novo>salario_atual:
        print(f'O novo salário é R$ {novo:.2f}')
    else:
        print(f'Não houve aumento')
    return novo

def main():
    salario_atual = float(input())
    tempo_servico = int(input())
    salary(salario_atual, tempo_servico)

main()



     
    