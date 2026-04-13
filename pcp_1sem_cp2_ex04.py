def calcular_horas_extras(salario_base, horas):
    horas_extras = (salario_base * horas) * (1.5 / 100)
    return horas_extras

def  calcular_descontos_falta(salario_base, faltas):
    desconto_faltas = (salario_base * faltas) * (2 / 100)
    return desconto_faltas

def calcular_bonus(cargo, recebeu_bonus):
    if recebeu_bonus == "s":
        if cargo == 1:
            bonus_recebido = 1000
            return bonus_recebido
        elif cargo == 2:
            bonus_recebido = 500
            return bonus_recebido
        elif cargo == 3:
            bonus_recebido = 300
            return bonus_recebido
        else:
            bonus_recebido = 100
            return bonus_recebido
    else:
        bonus_recebido = 0
        return bonus_recebido



nome_funcionario = input("Digite o nome do funcionário: ")
print("Selecione um cargo:"
      "\n1-Gerente"
      "\n2-Analista"
      "\n3-Assistente"
      "\n4-Estagiário")
cargo = int(input("Selecione: "))
sal_base = float(input("Digite o salário base: R$"))
total_h_trab = float(input("Digite o total de horas extras trabalhadas: "))
total_f_mes = float(input("Digite o total de faltas no mês: "))
bonus = input("O funcionário recebeu bonûs (s/n): ")

val_h_extra = calcular_horas_extras(sal_base, total_h_trab)
val_desc_faltas = calcular_descontos_falta(sal_base, total_f_mes)
val_bonus = calcular_bonus(cargo, bonus)

sal_bruto = sal_base + val_h_extra + val_bonus

print(f"\n====== {nome_funcionario} ======"
      f"\nSalário Bruto: R${sal_bruto}"
      f"\nTotal de acréscimos: R${val_h_extra + val_bonus}"
      f"\nTotal de descontos: R${val_desc_faltas}"
      f"\nSalario final: R${sal_bruto - val_desc_faltas}")
