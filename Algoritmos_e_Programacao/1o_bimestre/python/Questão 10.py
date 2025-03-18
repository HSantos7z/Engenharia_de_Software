#Lista de exercicios de entrada, processamento e saida no meu espaço da univille
#Questão número 10

print('Este programa calcula a distância entre 2 pontos')

x1 = int(input('Informe o primeiro ponto x1: '))
y1 = int(input('Informe o segundo ponto y1: '))
x2 = int(input('Informe o primeiro ponto x2: '))
y2 = int(input('Informe o segundo ponto y2: '))

distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print('A distância entre os pontos P e Q é:', distancia)