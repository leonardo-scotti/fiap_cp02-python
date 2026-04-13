cod_uf = int(input("Digite o código do estado de origem da carga (1 - 5): "))

if cod_uf == 1:
    imposto = 0.35
    imposto_texto = "35%"
elif cod_uf == 2:
    imposto = 0.25
    imposto_texto = "25%"
elif cod_uf == 3:
    imposto = 0.15
    imposto_texto = "15%"
elif cod_uf == 4:
    imposto = 0.05
    imposto_texto = "5%"
else:
    imposto = 0.0
    imposto_texto = "Isento (0%)"

peso = float(input("Digite o peso da carga em toneladas: "))
carga_kg = peso * 1000

cod_carga = int(input("Digite o código da carga (10 a 40): "))

if cod_carga >= 10 and cod_carga <= 20:
    preco_final = carga_kg * 100
elif cod_carga <= 30:
    preco_final = carga_kg * 250
else:
    preco_final = carga_kg * 340

valor_imposto = preco_final * imposto
valor_final = preco_final + valor_imposto

print("\n", "====== RELATÓRIO ======", "\n")
print(f"O peso da carga em kg é: {carga_kg:.2f} kg")
print(f"O preço da carga é: R$ {preco_final:.2f}")
print(f"O valor do imposto ({imposto_texto}): R$ {valor_imposto:.2f}")
print(f"O valor total é: R$ {valor_final:.2f}")