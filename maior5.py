def maior5(a: float, b: float, c:float, d:float, e:float)-> float:
    maior = a
    if b>maior:
        maior = b
    if c>maior:
        maior = c
    if d>maior:
        maior = d
    if e>maior:
        maior = e
    return maior

def main():
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    e = float(input())
    X = maior5(a, b, c, d, e)
    print(f"O maior valor é {X}")

main()

