def categoria_atleta(idade, peso):
    if (idade<10 and peso<30):
        print(f"Atleta não apto para competição")
    else:
        cat_idade = ""
        cat_peso = ""
        if 10<=idade<=13:
            cat_idade = "Infantil"
        elif 14<=idade<=17:
            cat_idade = "Juvenil"
        else:
            cat_idade = "Adulto"

        if 30<=peso<=60:
            cat_peso = "Leve"
        else:
            cat_peso = "Pesado"

        print(f"Categoria: {cat_idade} - {cat_peso}")

def main():
    idade=int(input())
    peso=float(input())
    categoria_atleta(idade,peso)
main()


