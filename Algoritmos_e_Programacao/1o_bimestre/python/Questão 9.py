#Lista de exercicios de entrada, processamento e saida no meu espaço da univille
#Questão número 9

print('Este programa calcula o valor gasto em tintas para pintar tanques cilíndricos')

# Caclcula primeiro a área

raio = float(input('Informe o raio do tanque '))
altura = float(input('Informe a altura do tanque '))

area = 2 * 3.14 * raio ** 2 + 2 * 3.14 * raio * altura

# Depois calcula a quantidade de litros de tinta

litros_tinta = area/3

# quantas latinhas são necessárias

latas = litros_tinta/5

# quanto custaria

custo = latas*20

print('A quantidade de latas necessárias são ', latas, 'E o custo total é ', custo)

