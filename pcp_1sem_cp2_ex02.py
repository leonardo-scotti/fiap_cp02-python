def ordenarLados(a, b, c):
    lista = [a, b, c]
    lista_ordenada = sorted(lista, reverse=True)
    return lista_ordenada

def verificar_triangulo(lados):
    a, b, c = lados

    if a >= b+c:
        print("NÃO FORMA TRIÂNGULO!")
        return

    if a**2 == b**2 + c**2:
        print("TRIÂNGULO RETÂNGULO.")
    elif a**2 > b**2 + c**2:
        print("TRIÂNGULO OBTUSÂNGULO.")
    elif a**2 < b**2 + c**2:
        print("TRIÂNGULO ACUTÂNGULO")

    if lados[0] == lados[1] == lados[2]:
        print("TRIÂNGULO EQUILÁTERO.")
    elif lados[0] == lados[1] or lados[1] == lados[2] or lados[0] == lados[2]:
        print("TRIÂNGULO ISÓCELES.")

print("Digite o valor de cada lado do triângulo:")
lado_a = float(input("Digite o lado A: "))
lado_b = float(input("Digite o lado B: "))
lado_c = float(input("Digite o lado C: "))

lados_triangulo = ordenarLados(lado_a, lado_b, lado_c)

verificar_triangulo(lados_triangulo)