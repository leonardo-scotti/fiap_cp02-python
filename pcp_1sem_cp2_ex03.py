vet_cp= []
vet_sp= []

for i in range(1,4):
    cp = float(input(f"Digite a nota do Checkpoint {i} (cp{i}): "))
    vet_cp.append(cp)

for i in range(1,3):
    sp = float(input(f"Digite a nota da Sprint {i} (sp{i}): "))
    vet_sp.append(sp)

gs = float(input("Digite a nota da Global Solution (gs): "))

menor_cp = vet_cp[0]

for i in vet_cp:
    if i < menor_cp:
        menor_cp = i

print(f"\nMenor nota entre os checkpoints: {menor_cp:.1f} (desconsiderada)")

soma_cp = sum(vet_cp) - menor_cp

media = (((soma_cp + sum(vet_sp)) / 4) * 0.4) + (gs * 0.6)

media_peso = media * 0.4
print("\n=== Resultados ===")
print(f"Média do semestre (sem peso): {media:.1f}")
print(f"Média do semestre (com peso): {media_peso:.1f}")
