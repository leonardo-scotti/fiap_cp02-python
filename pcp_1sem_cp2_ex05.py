def pode_aprovar(idade_cliente, renda_mensal, emprestimo_desejado):
    if idade_cliente < 18:
        print("Você não pode realizar o empréstimo. Idade menor que 18 anos.")
        return False

    if emprestimo_desejado > renda_mensal * 20:
        print("Você não pode realizar o empréstimo. Sua renda não é suficiente.")
        return False

    return True


def definir_taxas(parcelas_emprestimo):
    if parcelas_emprestimo < 6:
        return 0.05
    elif parcelas_emprestimo < 12:
        return 0.08
    else:
        return 0.10


def calcular_parcelas(emprestimo_desejado, parcelas_emprestimo, taxa_juros):
    fator = (1 + taxa_juros) ** parcelas_emprestimo
    pmt = emprestimo_desejado * (taxa_juros * fator) / (fator - 1)

    return pmt


def calcular_total(parcela, parcelas):
    return parcela * parcelas


def calcular_juros(total, valor_emprestimo):
    return total - valor_emprestimo

def main():
    nome_cliente = input("Digite seu nome: ")
    idade_cliente = int(input("Digite a sua idade: "))
    renda_mensal = float(input("Digite sua renda mensal: "))
    emprestimo_desejado = float(input("Digite o valor desejado do empréstimo: "))
    parcelas_emprestimo = int(input("Digite a quantidade de parcelas desejadas (3 - 24): "))

    if parcelas_emprestimo < 3 or parcelas_emprestimo > 24:
        print("Quantidade de parcelas inválida. Escolha entre 3 e 24.")
        return

    aprovado = pode_aprovar(idade_cliente, renda_mensal, emprestimo_desejado)

    if not aprovado:
        print("Empréstimo não aprovado.")
        return

    taxa_juros = definir_taxas(parcelas_emprestimo)

    valor_parcela = calcular_parcelas(
        emprestimo_desejado,
        parcelas_emprestimo,
        taxa_juros
    )

    total_pago = calcular_total(valor_parcela, parcelas_emprestimo)

    total_juros = calcular_juros(total_pago, emprestimo_desejado)

    print("\n===== RESULTADO DO EMPRÉSTIMO =====")
    print(f"Cliente: {nome_cliente}")
    print(f"Valor do empréstimo: R$ {emprestimo_desejado:.2f}")
    print(f"Parcelas: {parcelas_emprestimo}")
    print(f"Taxa de juros: {taxa_juros * 100:.2f}% ao mês")
    print(f"Valor da parcela: R$ {valor_parcela:.2f}")
    print(f"Total pago: R$ {total_pago:.2f}")
    print(f"Total de juros: R$ {total_juros:.2f}")

if __name__ == "__main__":
    main()