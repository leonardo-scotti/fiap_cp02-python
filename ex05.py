def coletar_dados():
    nome_cliente        = input("Digite seu nome: ")
    idade_cliente       = int(input("Digite a sua idade: "))
    renda_mensal        = float(input("Digite sua renda mensal: "))
    emprestimo_desejado = float(input("Digite o valor do empréstimo desejado: "))
    parcelas_emprestimo = int(input("Digite a quantidade de parcelas desejadas (3 - 24): "))
    return nome_cliente, idade_cliente, renda_mensal, emprestimo_desejado, parcelas_emprestimo


def pode_aprovar(idade_cliente, parcelas_emprestimo, emprestimo_desejado, renda_mensal):
    if idade_cliente < 18:
        print("Você não pode realizar o empréstimo. Idade menor que 18 anos.")
        return False

    if parcelas_emprestimo < 3 or parcelas_emprestimo > 24:
        print("Quantidade de parcelas deve ser entre 3 e 24.")
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
    PV = emprestimo_desejado
    n = parcelas_emprestimo
    i = taxa_juros

    fator = (1 + i) ** n
    PMT = PV * (i * fator) / (fator - 1)

    return PMT


def calcular_total(parcela, parcelas):
    return parcela * parcelas


def calcular_juros(total, valor_emprestimo):
    return total - valor_emprestimo


def exibir_resultado(nome, emprestimo, taxa, pmt, parcelas, total, juros):
    print("\nParabéns! Seu empréstimo foi aprovado, segue as informações:")
    print(f"Nome:              {nome}")
    print(f"Valor financiado:  R$ {emprestimo:.2f}")
    print(f"Taxa de juros:     {taxa * 100:.0f}% ao mês")
    print(f"Valor da parcela:  R$ {pmt:.2f}")
    print(f"Total a pagar:     R$ {total:.2f}")
    print(f"Total em juros:    R$ {juros:.2f}")


def main():
    nome, idade, renda, emprestimo, parcelas = coletar_dados()

    if pode_aprovar(idade, parcelas, emprestimo, renda):
        taxa = definir_taxas(parcelas)
        pmt = calcular_parcelas(emprestimo, parcelas, taxa)
        total = calcular_total(pmt, parcelas)
        juros = calcular_juros(total, emprestimo)

        exibir_resultado(nome, emprestimo, taxa, pmt, parcelas, total, juros)


main()