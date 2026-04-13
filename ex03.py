print("=== Calculadora de Médias ===\n")

cp1 = float(input("Digite a nota do Checkpoint 1 (cp1): "))
cp2 = float(input("Digite a nota do Checkpoint 2 (cp2): "))
cp3 = float(input("Digite a nota do Checkpoint 3 (cp3): "))
sp1 = float(input("Digite a nota da Sprint 1 (sp1): "))
sp2 = float(input("Digite a nota da Sprint 2 (sp2): "))
gs = float(input("Digite a nota da Global Solution (gs): "))

menor_cp = cp1
nome_menor = "cp1"

if cp2 < menor_cp:
    menor_cp = cp2
    nome_menor = "cp2"

if cp3 < menor_cp:
    menor_cp = cp3
    nome_menor = "cp3"

print(f"\nMenor nota entre os checkpoints: {nome_menor} = {menor_cp:.1f} (desconsiderada)")

soma_cp = cp1 + cp2 + cp3 - menor_cp

media = ((soma_cp + sp1 + sp2) / 4) * 0.4 + gs * 0.6

media_peso = media * 0.4
print("\n=== Resultados ===")
print(f"Média do semestre (sem peso): {media:.1f}")
print(f"Média do semestre (com peso): {media_peso:.1f}")


