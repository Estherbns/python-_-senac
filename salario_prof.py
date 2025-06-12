valor_hora_trab = float(input("informe valor hora:"))
num_horas_trab = float(input("informe o numero de horas trabalhada: "))
desc_inss = float(input("informe o desconto INSS: "))


valor_sal_bruto = (valor_hora_trab * num_horas_trab) 

desconto = desc_inss/100

valor_sal_liquido = valor_sal_bruto - (valor_sal_bruto * desconto)


print(f"o valor do salario é { valor_sal_liquido} para o professor" )