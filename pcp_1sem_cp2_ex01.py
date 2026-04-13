cod_uf = int(input("Digite o código do estado de origem da carga (1 - 5): "))
peso = float(input("Digite o peso da carga do caminhão em toneladas: "))
cod_carga = int(input("Digite o código da carga (10 a 40): "))

carga_kg = peso * 1000

impostos = {
    1: 0.35,
    2: 0.25,
    3: 0.15,
    4: 0.05,
    5: 0.0
}
impostos_texto = {
    1: "35%",
    2: "25%",
    3: "15%",
    4: "5%",
    5: "Isento (0%)"
}

imposto = impostos[cod_uf]
imposto_texto = impostos_texto[cod_uf]

if 10 <= cod_carga <= 20:
    preco_por_kg = 100
elif 21 <= cod_carga <= 30:
    preco_por_kg = 250
elif 31 <= cod_carga <= 40:
    preco_por_kg = 340

preco_final = carga_kg * preco_por_kg
valor_imposto = preco_final * imposto
valor_total = preco_final + valor_imposto

print("\n====== RELATÓRIO ======")
print(f"Peso da carga em kg: {carga_kg:.2f} kg")
print(f"Preço da carga: R$ {preco_final:.2f}")
print(f"Valor do imposto ({imposto_texto}): R$ {valor_imposto:.2f}")
print(f"Valor total transportado: R$ {valor_total:.2f}")
